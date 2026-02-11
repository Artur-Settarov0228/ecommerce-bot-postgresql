from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base import Base


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(BigInteger, primary_key=True)

    image_url = Column(String(500), nullable=False)

    product_id = Column(
        BigInteger,
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
    )

    product = relationship(
        "Product",
        back_populates="images",
    )
