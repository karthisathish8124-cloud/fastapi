from fastapi import FastAPI, Depends

def token(tok:str="123"):
    if tok!="123":
        raise Exception("token invalid")
    return True

app = FastAPI(dependencies=[Depends(token)])

@app.get("/display")
def dis():
    return {"message": "hello"}
