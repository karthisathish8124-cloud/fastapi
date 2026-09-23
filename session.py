from fastapi import FastAPI, Cookie, Response, HTTPException
from typing import Optional
import uuid

app = FastAPI()

cname = "sathish"
cpass = "7777"

session = {}

@app.post("/login/")
def login(username: str, password: str, res: Response):
    if username == cname and password == cpass:
        sid = str(uuid.uuid4())
        session[sid] = {"username": username}
        res.set_cookie(key="sid", value=sid, httponly=True)
        return {"message": "success"}
    else:
        raise HTTPException(status_code=401, detail="invalid credentials")

@app.get("/home/")
def homepage(sid: Optional[str] = Cookie(None)):
    if sid is None or sid not in session:
        raise HTTPException(status_code=401, detail="not authenticated")
    return {"user": session[sid]}
