from pydantic import BaseModel
from datetime import datetime


class QuestionsParameters(BaseModel):
    questions_num: int


class CategorySchema(BaseModel):

    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    clues_count: int
    #
    # class Config:
    #     from_attributes = True


class QuestionSchema(BaseModel):

    id: int
    answer: str
    question: str
    value: int | None
    airdate: datetime
    created_at: datetime
    updated_at: datetime
    category_id: int
    game_id: int
    invalid_count: int | None
    category: CategorySchema

    # class Config:
    #     from_attributes = True
