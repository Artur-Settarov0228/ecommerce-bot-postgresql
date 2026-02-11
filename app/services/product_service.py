from models.product import Product
from repositories.product_repo import ProductRepository


class ProductService:

    @staticmethod
    def create_product(db, name, price, stock, category_id):
        if price <= 0:
            raise ValueError("Narx noto‘g‘ri")

        product = Product(
            name=name,
            price=price,
            stock=stock,
            category_id=category_id,
        )
        return ProductRepository.create(db, product)

    @staticmethod
    def update_stock(db, product_id: int, quantity: int):
        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            raise ValueError("Product topilmadi")

        if product.stock < quantity:
            raise ValueError("Stock yetarli emas")

        product.stock -= quantity
        return ProductRepository.update(db, product)
