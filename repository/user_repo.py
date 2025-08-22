from model.user import User
from sqlalchemy.orm import Session
class userRepository:
    #constructor
    #db session from sqlalchemy is stored in every object
    def __init__(self, db:Session):
        self.db = db

    def get_all_users(self):

        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):

        return self.db.query(User).filter(User.id == user_id).first()


    def get_user_by_username(self, username: str):

        return self.db.query(User).filter(User.username == username).first()

    def add_user(self, username: str, email: str, password: str):

        new_user = User(username = username, email = email, password_hash = password)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self, user_id: int, username: str = None, email: str = None):

        user = self.get_user_by_id(user_id)

        if not user:
            return None
        if username:
            user.username = username
        if email:
            user.email = email
        self.db.commit()
        self.db.refresh(user)
        return user


    def delete_user(self, user_id):

        user = self.get_user_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True

    # @staticmethod
    # def get_all_users(db:Session):
    #     #querying user table
    #     return db.query(User).all()


    # @staticmethod
    # def get_user_by_id(db: Session, user_id: int):
    #     #filtering user table for user_id
    #     return db.query(User).filter(User.id == user_id).first()

    # @staticmethod
    # def get_user_by_username(db: Session, username: str):

    #     return db.query(User).filter(User.username == username).first()

    # @staticmethod
    # def add_user(db: Session, username: str, email: str, password: str):

    #     new_user = User(username = username, email = email, password_hash = password)
    #     db.add(new_user)
    #     db.commit()
    #     db.refresh(new_user)
    #     return new_user

    # @staticmethod
    # def update_user(db: Session, user_id: int, new_username: str = None, email: str = None):
    #     user = user_repo.get_user_by_id(db, user_id)
    #     if user:
    #         if new_username:
    #             user.username = new_username
    #         if email:
    #             user.email = email
    #         db.commit()
    #         db.refresh(user)
    #         return user
    #     return None



    # @staticmethod
    # def delete_user(db:Session, user_id: int):
    #     user = user_repo.get_user_by_id(db, user_id)
    #     if user:
    #         db.delete(user)
    #         db.commit()
    #         return True
    #     return False
