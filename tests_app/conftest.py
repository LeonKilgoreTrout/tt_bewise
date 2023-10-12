from app.main import app
from app.models import Base
from app.settings import Settings
from app.services import get_db
import pytest
from sqlalchemy import create_engine, orm


DB_URL = "sqlite:///./test.db"
engine = create_engine(DB_URL, connect_args={'check_same_thread': False})
TestingSession = orm.sessionmaker(autoflush=False, autocommit=False, bind=engine)


def override_get_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield override_get_db
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db
