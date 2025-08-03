from db import SessionLocal
from model.user import User
from model.category import Category
from model.expense import Expense
from datetime import date
from decimal import Decimal

#create a new session
session = SessionLocal()

try:
   # Step 1: Create and commit the user
    user = User(username="john_doe", email='johnDoe@gmail.com', password_hash="secure123")
    session.add(user)
    session.commit()
    session.refresh(user)  # Get the generated user.id

    # Step 2: Create and commit the category
    category = Category(name="groceries", user_id=user.id)
    session.add(category)
    session.commit()
    session.refresh(category)  # Get the generated category.id

    # Step 3: Create and commit the expense
    expense = Expense(
        amount='45.76',
        description="weekly food from costco",
        date=date.today(),
        user_id=user.id,
        category_id=category.id
    )
    session.add(expense)
    session.commit()

    print("User :", user.username," : ",user.id)
    print("category :", category.name," : ",category.id)
    print("expense amount: ", expense.amount,", expense description: ",expense.description,", expense user_id: ", expense.user_id,", expense category_id: ", expense.category_id)

except Exception as e:
    
    session.rollback()
    print("Error:", e)
finally:
    session.close()