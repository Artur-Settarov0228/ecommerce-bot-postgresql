from app.models.base import Base
from app.core.database import engine

# MUHIM: hamma modellar import qilinishi SHART
from app.models.user import User
from app.models.order import Order
from app.models.categories import Categorie
from app.models.product import Product
from app.models.product_image import ProductImage


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
