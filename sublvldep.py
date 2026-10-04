from fastapi import FastAPI,Depends

app = FastAPI()

def gp():
    return{"grandparent":"connected"}
def p(a=Depends(gp)):
    return {"parent": "connected", **a}

@app.get("/display")
def child(b=Depends(p)):
    return {"child": "connected", **b}
