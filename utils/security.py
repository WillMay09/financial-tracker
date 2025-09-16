import bcrypt

def hash_password(password: str) -> str:

    #generate salt
    salt = bcrypt.gensalt()
    
    hashed_password = bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)

    return hashed_password.decode('utf-8')


def verifyPassword(password: str, hashed_password: str)-> bool:

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

