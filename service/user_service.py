from repository.user_repo import userRepository
from decimal import Decimal
from datetime import date
import re
import bcrypt
from utils.security import hash_password, verify_password

class userService:

    def __init__(self, user_repo : userRepository):

        self.user_repo = user_repo

    def get_user_by_id(self, user_id: int):

        #checks if user_id is a number
        if not isinstance(user_id, int) or user_id <=0:
            raise ValueError("Invalid User Id")

        #checks if user exists
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")

        return user
        
    
    def get_user_by_username(self, username: str):

        user = self.user_repo.get_user_by_username(username)

        if not user:
            ValueError(f"Username with name: {username} does not exist")

        return user


    def add_user(self, username: str, email: str, password: str):

        #cannot be empty
        if not username.strip():
            raise ValueError("Username cannot be empty")
        #over 30 characters
        if len(username) > 30:
            raise ValueError("Username cannot be longer than 30 characters")

        #checks if username contains only numbers, letters, and underscores use reg ex
        if not re.match(r"^[\w]+$", username):
            raise ValueError("Username can only contain numbers, letters and underscores")
        
        #ensures correct email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email not properly formatted")

        if len(password) < 8:
            raise ValueError("Password must be atleast 8 characters long")

        #Ensure uniqueness
        if self.user_repo.get_user_by_username(username):
            raise ValueError("Username already exists")

        #hash password
        hashed_password = hash_password(password)
        

        return self.user_repo.add_user(username, email, hashed_password)


        #--------------------Update-----------------------#
        def update_user_email(self, user_id: int, new_email: str)
            if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                raise ValueError("Invalid email format")


            return self.user_repo.update_user(user_id, new_email)

        
        def delete_user(self, user_id :int):

            if self.user_repo.delete_user(user_id: int):
                return True
            else:
                raise ValueError("User not found")


    

      



    