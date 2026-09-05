from fastapi import FastAPI,File,UploadFile
import pandas as pd 
from PyPDF2 import PdfReader
import io 

app = FastAPI()

@app.post("/pdfandexcel")
async def pdfexcel(file:UploadFile = File(...)):
    content=await file.read()
    name= file.filename.lower()

    if name.endswith((".xls",".xlsx")):
        excel=pd.read_excel(io.BytesIO(content))
        return{
            "type":"excel"
        }
    elif name.endswith(".pdf"):
        pdf=PdfReader(io.BytesIO(content))
        text = "".join([p.extract_text() or "" for p in pdf.pages])
        return{
            "type":"pdf",
            "preview":text.strip()[:200]
        }

    return {"error": "unsupported file"}    
