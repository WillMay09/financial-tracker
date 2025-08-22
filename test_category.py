import pytest
from db import SessionLocal
from repository.category_repo import CategoryRepository
from model.category import Category
from model.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base

#created fresh for every test function
@pytest.fixture(scope='function')
def db_session():

    #selects all rows in expense table, deletes
    """ create an in-memory SQLite session for testing"""
    engine = create_engine("sqlite:///:memory: ", echo=False)
    #session factory that makes sessions with the previous engine
    TestingSessionLocal = sessionmaker(bind=engine)
    #drops all tables before recreating them
    Base.metadata.drop_all(bind=engine)
    #creates tables from orm models
    Base.metadata.create_all(bind=engine)
    #new db session that will be used during the test
    session = TestingSessionLocal()
    
    try:
        #provides session to the test, after test is done, code after yields(clean up)
        yield session
    finally:
        #closes session
        session.close()

#this decorator tells pytest this is a factory that returns something useful for my tests
@pytest.fixture
def repo(db_session):
    return CategoryRepository(db_session)

#db_session is called before every test
def test_add_category(repo):

    new_category = repo.add_category("food", 5)
    #object first, then class
    assert isinstance(new_category, Category)
    assert new_category.name == "food"
    assert new_category.user_id == 5

def test_get_all_categories(repo):

    new_category1 = repo.add_category("tech", 6)
    new_category2 = repo.add_category("rent", 7)

    categories = repo.get_all_categories()
    assert isinstance(categories, list)
    assert len(categories) >= 2
    

def test_get_category_by_name(repo):
    repo.add_category("new_category", 5)
    found_category = repo.get_category_by_name("new_category")

    assert found_category is not None
    assert found_category.name =="new_category"
    assert found_category.user_id == 5

def test_get_category_by_id(repo):

    new_category = repo.add_category("another_category", 5)
    found_category = repo.get_category_by_id(new_category.id)
    assert found_category is not None
    assert found_category.name == 'another_category'
    assert found_category.user_id == new_category.user_id

def test_delete_category(repo):

    new_category = repo.add_category("temp_category", 5)
    result = repo.delete_category(new_category.id)
    assert result is True
    assert repo.get_category_by_id(new_category.id) is None



#   @staticmethod
#     def get_all_categories(db:Session)
#         return db.query(Category).all()

#     @staticmethod
#     def get_category_by_name(db:Session,name: str):

#         return db.query(Category).filter(Category.name == name).first()
    
#     @staticmethod
#     def get_category_by_id(db:Session,category_id:int):

#         return db.query(Category).filter(Category.category_id == category_id).first()

#     @staticmethod
#     def get_category_by_user_id(db:Session,user_id: int):

#         return db.query(Category).filter(Category.user_id== user_id).all()

#     @staticmethod
#     def add_category(db: Session, name: str, user_id: int)

#         new_category = Category(name=name, user_id=user_id)
#         db.add(new_category)
#         db.commit()
#         db.refresh(new_category)
#         return new_category

#     @staticmethod
#     def delete_category(db: Session, category_id:int):
        
#         category = db.query(Category).filter(Category.id == category_id).first()
#         if category:
#             db.delete(category)
#             db.commit()
#             db.refresh(category)
#             return True
#         return False