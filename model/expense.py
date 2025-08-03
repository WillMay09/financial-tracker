from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Numeric
from model.base import Base


class Expense(Base):

    __tablename__='expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(String(300), nullable=True)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
