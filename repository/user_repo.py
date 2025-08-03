from model.user import User
from sqlalchemy.orm import Session
class user_repo:

    @staticmethod
    def get_all_users(db:Session):
        #querying user table
        return db.query(User).all()


    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        #filtering user table for user_id
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):

        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def add_user(db: Session, username: str, email: str, password: str)

        new_user = User(username = username, email = email, password_hash = password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def update_user(db: Session, username: str = None, email: str = None):
        user = user_repo.get_user_by_username(db, username)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            db.commit()
            db.refresh(user)
            return user
        return None



    @staticmethod
    def delete_user(db:Session, user_id: int):
        user = user_repo.get_user_by_id(db, user_id)
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
