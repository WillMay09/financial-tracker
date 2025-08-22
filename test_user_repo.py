import pytest
#a unit to work with the db
from db import SessionLocal
from repository.user_repo import userRepository 
#used for type checking
from model.user import User
from model.category import Category
from model.expense import Expense
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base

#tells pytest to use as setup code
@pytest.fixture
def db_session():
    
    engine = create_engine("sqlite:///memory:", echo=False)
    TestingSessionLocal = sessionmaker(bind=engine)
    #clean up before test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture

def repo(db_session):

    return userRepository(db_session)



def test_create_user(repo):
    user = repo.add_user("testuser","test@example.com", "hashed123")
    #verifies this is indeed a user instance
    assert isinstance(user, User)
    #verifies username is correct
    assert user.username == "testuser"

def test_get_user_by_username(repo):
    user = repo.add_user("anotheruser", "another@example.com", "hashed345")
    #searching for user based on username just created
    found_user = repo.get_user_by_username("anotheruser")
    #verifying the user is returned
    assert found_user is not None
    #verifying the username
    assert found_user.username == "anotheruser"
    assert found_user.email == "another@example.com"

def test_user_by_id(repo):
    new_user = repo.add_user("newUser", "user@gmail.com","hashed123")
    fetched = repo.get_user_by_id(new_user.id)
    assert fetched is not None
    assert fetched.id == new_user.id

def test_get_all_users(repo):
    repo.add_user("user1", "user1@example.com", "pw1")
    repo.add_user("user2", "user2@example.com", "pw2")
    all_users = repo.get_all_users()
    #asserting that this is in fact a list
    assert isinstance(all_users, list)
    assert len(all_users) >=2

def test_update_user(repo):
    user = repo.add_user("oldName", "old@example.com", "oldhash")

    updated = repo.update_user(user.id, 'newname',"new@example.com")
    assert updated.username == "newname"
    assert updated.email == "new@example.com"

def test_delete_user(repo):

    user = repo.add_user("tobedeleted", "del@example.com", "delhash")
    result = repo.delete_user(user.id)
    assert result is True
    assert repo.get_user_by_id(user.id) is None



#  @staticmethod
#     def get_all_users(db:Session):
#         #querying user table
#         return db.query(User).all()


#     @staticmethod
#     def get_user_by_id(db: Session, user_id: int):
#         #filtering user table for user_id
#         return db.query(User).filter(User.id == user_id).first()

#     @staticmethod
#     def get_user_by_username(db: Session, username: str):

#         return db.query(User).filter(User.username == username).first()

#     @staticmethod
#     def add_user(db: Session, username: str, email: str, password: str)

#         new_user = User(username = username, email = email, password_hash = password)
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return new_user

#     @staticmethod
#     def update_user(db: Session, username: str = None, email: str = None):
#         user = user_repo.get_user_by_username(db, username)
#         if user:
#             if username:
#                 user.username = username
#             if email:
#                 user.email = email
#             db.commit()
#             db.refresh(user)
#             return user
#         return None



#     @staticmethod
#     def delete_user(db:Session, user_id: int):
#         user = user_repo.get_user_by_id(db, user_id)
#         if user:
#             db.delete(user)
#             db.commit()
#             return True
#         return False

