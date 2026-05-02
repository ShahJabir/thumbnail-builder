"""Database connection and operations"""

from sqlmodel import SQLModel, create_engine, Session
from config import DATABASE_URL

engine = create_engine(
    DATABASE_URL, echo=False, connect_args={"check_same_thread": False}
)


def create_tables():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session
