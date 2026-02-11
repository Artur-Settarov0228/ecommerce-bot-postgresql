from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User


class UserService:

    @staticmethod
    def get_or_create(db: Session, telegram_id: int, full_name: str):
        user = db.execute(
            select(User).where(User.telegram_id == telegram_id)
        ).scalar_one_or_none()

        if not user:
            user = User(
                telegram_id=telegram_id,
                full_name=full_name,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        return user
