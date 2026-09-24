
from fastapi import FastAPI,Cookie,Response,HTTPException
from typing import Optional
import uuid
from datetime import datetime ,timedelta
app=FastAPI()

cname="sathish"
cpass="7777"

session={}
time=10

@app.post("/login/")
def login(username: str, password: str, res: Response):
    if username==cname and password==cpass:
        exp_time=datetime.now()+timedelta(seconds=10)
        sid=str(uuid.uuid4())
        session[sid]={"username":username,"exp_time":exp_time}
        res.set_cookie(key="sid",value=sid,httponly=True,max_age=time)
        return{"message":"success"}
    
    else:
        raise HTTPException(status_code=401,detail="invalid credentials")

@app.get("/home/")
def homepage(sid: Optional[str] = Cookie(None)):
    if sid is None or sid not in session:
        raise HTTPException(status_code=401,detail="not authenticated")

    session_data=session[sid]
    if session_data["exp_time"]<datetime.now():
        session.pop(sid)
    return{"data":session}