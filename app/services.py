from .database import SessionLocal
from fastapi import HTTPException
from .logger import log
from .models import Category, Question
import requests
from .schemas import QuestionsParameters, QuestionSchema, CategorySchema
from typing import List


URL = "https://jservice.io/api/random?count="
cached_question: QuestionSchema | None = None


def _get_questions(questions_num: int) -> List[QuestionSchema]:
    url = f"{URL}{questions_num}"
    questions = requests.get(url=url).json()
    questions = [QuestionSchema(**question) for question in questions]
    return questions


def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def _get_question(question: QuestionSchema,
                        db: SessionLocal) -> QuestionSchema:
    question_ = db.query(Question).filter(Question.id == question.id).first()
    if question_:
        return question
    detail = f"Question {question.id} does not exist"
    raise HTTPException(status_code=404, detail=detail)


async def _get_category(category: CategorySchema,
                        db: SessionLocal) -> CategorySchema:
    category_ = db.query(Category).filter(Category.id == category.id).first()
    if category_:
        return category
    detail = f"Question {category.id} does not exist"
    raise HTTPException(status_code=404, detail=detail)


async def _add_category(category: CategorySchema,
                        db: SessionLocal) -> CategorySchema:
    try:
        await _get_category(category=category, db=db)
    except HTTPException:
        category_fields = category.model_dump()
        category_ = Category(**category_fields)
        db.add(category_)
        db.commit()
        db.refresh(category_)
        log(f"Category {category.id} saved", model=category_fields)
        return category
    detail = f"Category {category.id} already exists"
    raise HTTPException(status_code=409, detail=detail)


async def _add_question(question: QuestionSchema,
                        db: SessionLocal) -> QuestionSchema:
    try:
        await _get_question(question=question, db=db)
    except HTTPException:
        try:
            await _add_category(question.category, db=db)
        except HTTPException:
            log(message=f"Attempted to save category {question.category.id}. But it already exists.")
        question_fields = question.model_dump()
        del question_fields["category"]
        question_ = Question(**question_fields)
        db.add(question_)
        db.commit()
        db.refresh(question_)
        log(f"Question {question.id} saved", model=question_fields)
        return question
    detail = f"Question {question.id} already exists"
    log(message=detail)
    raise HTTPException(status_code=409, detail=detail)


async def _add_questions(parameters: QuestionsParameters,
                         db: SessionLocal) -> QuestionSchema | None:
    global cache
    questions_num = parameters.questions_num
    if questions_num == 0:
        return None
    _questions_added_to_db = []
    while questions_num - len(_questions_added_to_db):
        for question in _get_questions(questions_num - len(_questions_added_to_db)):
            try:
                added_to_db = await _add_question(question=question, db=db)
                _questions_added_to_db.append(added_to_db)
                cache = added_to_db
            except HTTPException:
                log(message=f"Attempted to save question {question.id}. But it already exists.")
                cache = None
        log(message=f"{len(_questions_added_to_db)}/"
                    f"{questions_num} were unique. Trying to fill again.")
    return cache
