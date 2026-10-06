
from fastapi import FastAPI , HTTPException
from jose import JWTError,jwt 
from datetime import datetime,timedelta


app = FastAPI()

ALGORITHM="HS256"
SECRET_KEY="admin123"
ACCESS_TOKEN_EXPIRE_MINUTES=10

def create_token(uname:str):
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload={"username":uname,"expiry":expire.timestamp()}
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)


def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return payload["username"]
    except JWTError:
        raise HTTPException(status_code=401,detail="invalid token")

@app.post("/login")
def login(uname:str,password:str):
    if uname=="admin" and password=="123":
        token=create_token(uname)
        return{"access token": token}
    return HTTPException(status_code=401,detail="invalid credentials")

@app.get("/securedata")
def sec_data(token:str):
    username=verify_token(token)
    return{"message":f"secure data{username}"}