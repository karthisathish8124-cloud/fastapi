from fastapi import FastAPI,Depends

app=FastAPI()

class userdetails():
    def __init__(self):
        self.name="sathish"
        self.age=21
def getuser():
    return userdetails()


@app.get("/display")
def dis(a:userdetails=Depends(getuser)):
    return{"name":a.name,"age":a.age}