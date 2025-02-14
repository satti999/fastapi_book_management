from sqlmodel import create_engine, SQLModel, Session

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/pfA_book_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

def init_db():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(e)

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        print(e)
