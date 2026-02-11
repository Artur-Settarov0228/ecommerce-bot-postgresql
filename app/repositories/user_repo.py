from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_telegram_id(db: Session, telegram_id: int):
        return db.execute(
            select(User).where(User.telegram_id == telegram_id)
        ).scalar_one_or_none()

    @staticmethod
    def create(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def save(db: Session):
        db.commit()
