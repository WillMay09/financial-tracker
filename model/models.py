class User:
    #constructor
    def __init__(self, id,username, email, password):

        self.__id = id
        self.__username = username
        self.__email = email
        self.__password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password

class Category:

    def __init__(self,id, name, user_id):

        self.__id = id
        self.__name = name
        self.__user_id = user_id

    @property
    def id(self):
        
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
    @property
    def name(self):
        
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def user_id(self):
        
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

class Expense:

    def __init__(self, id, amount, description, date):
        self.__id = id
        self.__amount = amount
        self.__description = description
        self.__date = date
    
    @property
    def id(self):
        
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
    @property
    def amount(self):
        
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
    
    @property
    def description(self):
        
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date)
        self.__date = date


    

    
