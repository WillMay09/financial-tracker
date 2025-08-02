from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import date
from model.base import Base

#instance of base class
#classes that inherit from the base class will be tracked by alchemy and considered tables


class User(Base):
    #class will map to a database table
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    

    
