from fastapi import Depends, FastAPI, Response, status
from .schemas import QuestionsParameters, QuestionSchema
from .services import get_db, _add_questions
from .settings import Settings
from sqlalchemy.orm import Session


app_description = Settings().app_description
app = FastAPI(**app_description)


@app.post("/api/questions", tags=["Questions"])
async def add_questions(parameters: QuestionsParameters,
                        response: Response,
                        db: Session = Depends(get_db)) -> QuestionSchema | None:

    last_question = await _add_questions(parameters=parameters, db=db)
    response.status_code = status.HTTP_201_CREATED if last_question else status.HTTP_204_NO_CONTENT

    return last_question
