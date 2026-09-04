from pydantic import BaseModel
from fastapi import FastAPI,Form,File,UploadFile
from typing import Optional


class manu(BaseModel):
    company:str
    place:str

class item (BaseModel):
    name: str
    price: float
    availability: Optional[bool]= None
    manufacture:manu



app = FastAPI()




@app.post("/display")
def qpara(data:item):
    return{"message": "item recived","data":data}
    
@app.post("/feedback/")
def feedback(name:str=Form(...),ratt:int=Form(...)):
    return{
        "status": "recived",
        "name":name,
        "ratting":ratt
    }

@app.post("/file/")
async def fileupla(file:UploadFile=File(...)):
    content= await file.read()
    try:
        text_p=content.decode("utf-8")[:200]
    except e:
        text_p="cant open"    
        
    return {

        "filename": file.filename,
        "fileconatant": file.content_type,
        "filelen": len(content),
        "text":text_p
    }