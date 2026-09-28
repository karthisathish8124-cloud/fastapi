from fastapi import FastAPI,Depends

app=FastAPI()

def dep():
    return{"db":"connected"}

@app.get("/display")
def dis(a:dict=Depends(dep)):
    return{"message":"success","db_status":a}