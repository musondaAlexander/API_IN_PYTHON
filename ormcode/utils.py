from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashing the password
def hashing_password(password: str):
    return pwd_context.hash(password)

#====================================================================================================
# Verifying the password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
