from model import Category
from sqlalchemy.orm import Session
class category_repo: 

    @staticmethod
    def get_all_categories(db:Session)
        return db.query(Category).all()

    @staticmethod
    def get_category_by_name(db:Session,name: str):

        return db.query(Category).filter(Category.name == name).first()
    
    @staticmethod
    def get_category_by_id(db:Session,category_id:int):

        return db.query(Category).filter(Category.category_id == category_id).first()

    @staticmethod
    def get_category_by_user_id(db:Session,user_id: int):

        return db.query(Category).filter(Category.user_id== user_id).all()

    @staticmethod
    def add_category(db: Session, name: str, user_id: int)

        new_category = Category(name=name, user_id=user_id)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

    @staticmethod
    def delete_category(db: Session, category_id:int):
        
        category = db.query(Category).filter(Category.id == category_id).first()
        if category:
            db.delete(category)
            db.commit()
            db.refresh(category)
            return True
        return False

