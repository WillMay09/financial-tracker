from model import Expense
from sqlalchemy.orm import Session
from datetime import date
from decimal import Decimal
class expense_repo:

    @staticmethod
    def get_all_expenses(db:Session):

        return db.query(Expense).all()


    @staticmethod
    def get_expense_by_id(db:Session, expense_id:int):

        return db.query(Expense).filter(Expense.id == expense_id).first()

    @staticmethod
    def get_expense_by_user(db:Session, user_id:int):

        return db.query(Expense).filter(Expense.user_id == user_id).all()

    @staticmethod
    def get_expense_by_category(db:Session, category_id:int):

        return db.query(Expense).filter(Expense.category_id == category_id).all()


    @staticmethod
    def add_expense(db:Session, amount: Decimal, description: str, expense_date: date, user_id: int, category_id: int ):

        new_expense = Expense(amount=amount, description=description, date=expense_date, user_id=user_id, category_id = category_id)
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense


    @staticmethod
    def delete_expense(db:Session, expense_id:int):

        expense = query(Expense).filter(Expense.id == expense_id).first()
        if expense:
            db.delete(expense)
            db.commit()
            db.refresh(expense)
            return True
        return False
