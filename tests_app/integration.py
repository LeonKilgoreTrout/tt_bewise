from app.main import app
from app.models import Category, Question
from app.schemas import CategorySchema
from httpx import AsyncClient
import pytest
from sqlalchemy import select


base_url = "http://test"


@pytest.mark.asyncio
async def test_saved_5(test_db):
    questions_num = 5
    async with AsyncClient(app=app, base_url=base_url) as ac:
        await ac.post("/api/questions", json={
            "questions_num": questions_num
        })
    db = next(test_db())
    questions = db.query(Question).all()
    assert len(questions) == questions_num


@pytest.mark.asyncio
async def test_saved_300(test_db):
    questions_num = 300
    async with AsyncClient(app=app, base_url=base_url) as ac:
        await ac.post("/api/questions", json={
            "questions_num": questions_num
        })
    db = next(test_db())
    questions = db.query(Question).all()
    assert len(questions) == questions_num


@pytest.mark.asyncio
async def test_question_category_relation(test_db):
    questions_num = 2
    async with AsyncClient(app=app, base_url=base_url) as ac:
        await ac.post("/api/questions", json={
            "questions_num": questions_num
        })
    db = next(test_db())
    joined_question_query = select(Question, Category).join(Question)
    question, category = db.execute(joined_question_query).first()
    assert isinstance(question, Question)
    assert isinstance(category, Category)

    category = CategorySchema(**category.__dict__)
    assert len(category.model_fields_set) == 5
