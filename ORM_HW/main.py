from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Создание базы для SQLAlchemy
Base = declarative_base()

# Модели данных
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='products')
    prices = relationship('Price', back_populates='product')

class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    value = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    product = relationship('Product', back_populates='prices')

# Инициализация базы данных
engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Заполнение базы данных тестовыми данными
def populate_data():
    electronics = Category(name="Electronics")
    clothing = Category(name="Clothing")

    session.add_all([electronics, clothing])
    session.commit()

    phone = Product(name="Smartphone", category_id=electronics.id)
    tshirt = Product(name="T-shirt", category_id=clothing.id)

    session.add_all([phone, tshirt])
    session.commit()

    price1 = Price(product_id=phone.id, value=699.99)
    price2 = Price(product_id=tshirt.id, value=19.99)

    session.add_all([price1, price2])
    session.commit()

    print("Data populated successfully.")

# Выборка данных
def query_data():
    products = session.query(Product).all()
    for product in products:
        print(f"Product: {product.name}, Category: {product.category.name}")
        for price in product.prices:
            print(f"  Price: {price.value}, Date: {price.date}")

# Главная функция
if __name__ == "__main__":
    print("1. Populate database with test data")
    print("2. Query data from database")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        populate_data()
    elif choice == "2":
        query_data()
    else:
        print("Invalid choice. Exiting.")
