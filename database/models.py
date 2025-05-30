from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    is_admin = Column(Boolean, default=False)

    cart = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    image_url = Column(String)
    is_available = Column(Boolean, default=True)


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('cart.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)

    product = relationship("Product")


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="cart")
    items = relationship("CartItem")


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime)
    payment_method = Column(String)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem")


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)

    product = relationship("Product")