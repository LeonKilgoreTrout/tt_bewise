from fastapi import Depends, FastAPI, Response, status
from app.schemas import QuestionsParameters, QuestionResponse
from app.services import get_db, _add_questions
from app.settings import Settings
from sqlalchemy.orm import Session
from typing import Dict


app_description = Settings().app_description
app = FastAPI(**app_description.model_dump())


@app.post("/api/questions", tags=["Questions"], status_code=status.HTTP_200_OK)
async def add_questions(parameters: QuestionsParameters,
                        db: Session = Depends(get_db)) -> QuestionResponse:
    # FixMe: не смог определиться какой статус код возвращать (201 или 204)
    #  решил остановиться на 200 :)
    question = await _add_questions(parameters=parameters, db=db)

    return question
