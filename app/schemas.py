from pydantic import BaseModel, PositiveInt, NonNegativeInt
from datetime import datetime


class QuestionsParameters(BaseModel):
    questions_num: NonNegativeInt


class CategorySchema(BaseModel):

    id: PositiveInt
    title: str
    created_at: datetime
    updated_at: datetime
    clues_count: NonNegativeInt


class QuestionSchema(BaseModel):

    id: PositiveInt
    answer: str
    question: str
    value: NonNegativeInt | None
    airdate: datetime
    created_at: datetime
    updated_at: datetime
    category_id: PositiveInt
    game_id: PositiveInt
    invalid_count: NonNegativeInt | None
    category: CategorySchema


class QuestionResponse(BaseModel):
    penultimate_question: QuestionSchema | None
