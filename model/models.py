from sqlalchemy import Column, Integer, String, Float, Date, ForeignKEy
from sqlalchemy.orm import ,relationshipdeclarative_base
from datetime import date

#instance of base class
Base = declarative_base()

class User(Base):
    #class will map to a database table
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
class Category:

    __table__='categories'

        id = Column(Integer, primary_key=True)
        name = Column(String(100) unique=True, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        #Relationships
        user = relationship("User", back_populates="categories")
        expenses = relationship("Expense", back_populates="category", cascade="all, delete")

class Expense:

    __tables__='expenses'
        id = Column(Integer, primary_key=True)
        amount = Column(Integer, nullable=False)
        description = Column(String(300), nullable=True)
        date = Column(date, nullable=False)

        user_id = Column(Integer, ForeignKey('users.id'))
        category = Column(String(100), ForeignKey('categories.id'))

        user = relationship("User", back_populates="expenses")
        category = relationship("Category", back_populates="expenses")
   


    

    
