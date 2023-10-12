from app.main import app
from app.schemas import QuestionSchema, CategorySchema, QuestionsParameters
from httpx import AsyncClient
import pytest


base_url = "http://test"


@pytest.mark.anyio
async def test_post_5(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
            "questions_num": 5
        })
        assert response.status_code == 201
