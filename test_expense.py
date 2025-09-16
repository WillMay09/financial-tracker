from model.expense import Expense
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from datetime import date
from decimal import Decimal

import pytest
from repository.expenses_repo import ExpenseRepository


@pytest.fixture(scope='function')
def db_session():

    engine = create_engine("sqlite:///:memory:", echo=False)
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def repo(db_session):
    return ExpenseRepository(db_session)

def test_add_expense(repo):
    new_expense = repo.add_expense(12.54, "chocolate", date(2024, 11, 12), 1, 1)

    assert isinstance(new_expense, Expense)
    assert new_expense.amount == Decimal("12.54")
    assert new_expense.description == "chocolate"
    assert new_expense.user_id == 1

def test_get_all_expenses(repo):
    new_expense = repo.add_expense(12.54, "chocolate", date(2024, 11, 12), 1, 1)
    new_expense2 = repo.add_expense(45.67, "weekly groceries", date(2025, 8, 25), 2, 2)

    expenses = repo.get_all_expenses()
    assert isinstance(expenses, list)
    assert len(expenses) >=2
    
    

def test_get_expense_by_id(repo):
    new_expense = repo.add_expense(12.54, "chocolate", date(2024, 11, 12), 1, 1)
    found_expense = repo.get_expense_by_id(new_expense.id)
    assert found_expense is not None
    assert found_expense.amount == Decimal("12.54")
    assert found_expense.description == "chocolate"


def test_get_expense_by_user(repo):
    repo.add_expense(5.0, "snack", date(2024, 11, 15), user_id=1, category_id=1)
    repo.add_expense(50.0, "shoes", date(2024, 11, 16), user_id=2, category_id=1)
    user1_expenses = repo.get_expense_by_user(1)
    assert len(user1_expenses) == 1
    assert user1_expenses[0].description == "snack"


def test_delete_expense(repo):

    expense = repo.add_expense(30.0, "book", date(2024, 11, 17), 1, 1)
    result = repo.delete_expense(expense.id)
    assert result is True
    assert repo.get_expense_by_id(1) is None

