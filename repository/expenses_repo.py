from model import Expense
from sqlalchemy.orm import Session
from datetime import date
from decimal import Decimal

class ExpenseRepository:

    def __init__(self, db:Session):
        self.db = db

    def get_all_expenses(self):

        return self.db.query(Expense).all()

    def get_expense_by_id(self, expense_id: int):

        return self.db.query(Expense).filter(Expense.id == expense_id).first()

    def get_expense_by_user(self, user_id: int):

        return self.db.query(Expense).filter(Expense.user_id == user_id).all()


    def add_expense(self, amount: Decimal, description: str, date : date, user_id: int, category_id: int):

        new_expense = Expense(amount = amount, description = description, date = date, user_id = user_id, category_id = category_id)
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)
        return new_expense 
    

    def delete_expense(self, expense_id:int):

        expense = self.get_expense_by_id(expense_id)
        if expense:
            self.db.delete(expense)
            self.db.commit()
            return True
        return False




