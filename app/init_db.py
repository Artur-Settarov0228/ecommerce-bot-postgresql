# app/init_db.py
import app.models  # ❗ MUHIM: mapper registry to‘lishi uchun

from app.models.base import Base
from app.core.database import engine


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
