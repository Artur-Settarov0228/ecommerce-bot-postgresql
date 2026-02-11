from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.product import Product


class ProductRepository:

    @staticmethod
    def create(db: Session, product: Product) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_by_id(db: Session, product_id: int) -> Product | None:
        return db.execute(
            select(Product).where(Product.id == product_id)
        ).scalar_one_or_none()

    @staticmethod
    def get_all(db: Session):
        return db.execute(
            select(Product)
        ).scalars().all()

    @staticmethod
    def update(db: Session, product: Product) -> Product:
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete(db: Session, product: Product):
        db.delete(product)
        db.commit()
