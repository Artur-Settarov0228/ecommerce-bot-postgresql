from app.models.order import Order
from app.models.order_items import OrderItem

from app.repositories.order_repo import OrderRepository
from app.repositories.product_repo import ProductRepository


class OrderService:

    @staticmethod
    def add_to_cart(db, user_id: int, product_id: int, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity noto‘g‘ri")

        product = ProductRepository.get_by_id(db, product_id)
        if not product:
            raise ValueError("Mahsulot topilmadi")

        if product.stock < quantity:
            raise ValueError("Omborda yetarli mahsulot yo‘q")

        order = OrderRepository.get_pending_order(db, user_id)

        if not order:
            order = Order(
                user_id=user_id,
                total_price=0,
                status="pending",
            )
            order = OrderRepository.create_order(db, order)

        item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity,
            price=product.price,
        )
        OrderRepository.add_item(db, item)

        product.stock -= quantity
        order.total_price += product.price * quantity

        ProductRepository.save(db)
        OrderRepository.save(db)

        return order
