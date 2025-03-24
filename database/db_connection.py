from sqlmodel import create_engine, SQLModel, Session
from contextlib import contextmanager
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # Add echo for debugging


def init_db():
    """Initialize the database and create tables."""
    try:
        SQLModel.metadata.create_all(engine)
        print(" Database initialized successfully!")
    except Exception as e:
        print(f" Error initializing database: {e}")


@contextmanager
def get_session():
    """Provide a transactional scope around a series of operations."""
    session = Session(engine)
    try:
        yield session
        session.commit()  #  Ensure commits are handled
    except Exception as e:
        session.rollback()  #  Rollback on error
        print(f" Database session error: {e}")
    finally:
        session.close()  #  Always close session
