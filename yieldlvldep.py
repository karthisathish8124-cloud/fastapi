from fastapi import FastAPI, Depends
from datetime import datetime


app = FastAPI()

def shelf():
    print("book is taken from shelf",datetime.now())
    Book="fastapi book"
    yield Book
    print("book returned to self ",datetime.now())

@app.get("/display")
def read(a=Depends(shelf)):
    return {f"display_{datetime.now()}": f"reading {a}"}

