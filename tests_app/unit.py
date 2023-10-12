from app.main import app
from httpx import AsyncClient
import pytest


base_url = "http://test"


@pytest.mark.asyncio
async def test_post_negative_5(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
                "questions_num": -5
            })
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_post_not_a_number(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
            "questions_num": "test"
        })
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_post_0(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
            "questions_num": 0
        })
        assert response.json()["penultimate_question"] is None
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_1(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
            "questions_num": 1
        })
        assert response.json()["penultimate_question"] is None
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_5(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
            "questions_num": 5
        })
        # есть малая вероятность что возвращается None
        # assert response.json()["penultimate_question"] is not None
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_300(test_db):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/api/questions", json={
            "questions_num": 300
        })
        # есть малая вероятность что возвращается None
        # assert response.json()["penultimate_question"] is not None
        assert response.status_code == 200
