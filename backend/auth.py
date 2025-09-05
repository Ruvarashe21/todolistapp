import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User

# Secret key for JWT
SECRET_KEY = "mySecret"

# Password hashing 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

# Register a new user in the database
def register_user(email: str, password: str, db: Session):
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            return "User already exists"

        hashed_pw = hash_password(password)
        new_user = User(email=email, password_hash=hashed_pw)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "User registered"
    except Exception as e:
        print(f"Registration error: {e}")
        db.rollback()
        return f"Registration failed: {str(e)}"

# Log in and return a JWT token
def login_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return None  # Let your route handle the error

    token = jwt.encode(
        {
            "email": user.email,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    return token

# Validate token and return user info
def validate_token(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data["email"]
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
