from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.order import Order
from app.models.order_items import OrderItem


class OrderRepository:

    @staticmethod
    def get_pending_order(db: Session, user_id: int):
        return db.execute(
            select(Order).where(
                Order.user_id == user_id,
                Order.status == "pending",
            )
        ).scalar_one_or_none()

    @staticmethod
    def create_order(db: Session, order: Order):
        db.add(order)
        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def add_item(db: Session, item: OrderItem):
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def save(db: Session):
        db.commit()
