from fastapi import FastAPI, HTTPException, Depends, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models, database, auth
from routes import todo
from auth import register_user, login_user, validate_token
import logging
import datetime

#Test
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

print("Connected to:", database.engine.url)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.datetime.now()
    logger.info(f"Request: {request.method} {request.url}")
    
    try:
        response = await call_next(request)
        process_time = datetime.datetime.now() - start_time
        logger.info(f"Response: {response.status_code} - Time: {process_time}")
        return response
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        raise

origins = [
    "http://localhost:5174",
]
# CORS setup for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=database.engine)
app.include_router(todo.router)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model
class UserData(BaseModel):
    email: str
    password: str
    
@app.get("/")
def root():
    return {"message": "Todo API is running"}

# register route
@app.post("/register")
def register(user_data: UserData, db: Session = Depends(get_db)):
    logger.info(f"Registration attempt for: {user_data.email}")
    result = register_user(user_data.email, user_data.password, db)
    if result == "User already exists":
        logger.warning(f"Registration failed - user exists: {user_data.email}")
        raise HTTPException(status_code=409, detail=result)
    logger.info(f"User registered successfully: {user_data.email}")
    return {"message": result}

#  Login route
@app.post("/login")
def login(user_data: UserData, db: Session = Depends(get_db)):
    logger.info(f"Login attempt for: {user_data.email}")
    token = login_user(user_data.email, user_data.password, db)
    if not token:
        logger.warning(f"Login failed for: {user_data.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    logger.info(f"Login successful for: {user_data.email}")
    return {"token": token}

#  Protected route
@app.get("/protected")
def protected(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.warning("Protected route accessed without token")
        raise HTTPException(status_code=401, detail="Token required")
    token = authorization.split(" ")[1]
    result = validate_token(token)
    if result in ["Token has expired", "Invalid token"]:
        logger.warning(f"Protected route accessed with invalid token: {result}")
        raise HTTPException(status_code=401, detail=result)
    logger.info(f"Protected route accessed by: {result}")
    return {"message": f"Welcome {result}", "authenticated": True}

if __name__ == "__main__":
    import uvicorn
    print("Starting server on http://127.0.0.1:3002")
    print("If you can't access it, try: http://localhost:3002")
    uvicorn.run(app, host="127.0.0.1", port=3002, reload=False)
