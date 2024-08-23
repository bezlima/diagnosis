import bcrypt 

def encrypt_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def decrypt_password(login_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(login_password.encode('utf-8'), hashed_password.encode('utf-8'))