
from pydantic import BaseModel
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.openapi.utils import get_openapi
from typing import Optional, List


class manu(BaseModel):
    company: str
    place: str

class item(BaseModel):
    name: str
    price: float
    availability: Optional[bool] = None
    manufacture: manu


app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )
    for schema in openapi_schema.get("components", {}).get("schemas", {}).values():
        if isinstance(schema, dict) and "properties" in schema:
            for prop in schema["properties"].values():
                if prop.get("type") == "array" and "items" in prop:
                    if prop["items"].get("contentMediaType") == "application/octet-stream" or prop["items"].get("type") == "string":
                        prop["items"]["format"] = "binary"
                elif prop.get("contentMediaType") == "application/octet-stream":
                    prop["format"] = "binary"
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.post("/display")
def qpara(data: item):
    return {"message": "item received", "data": data}


@app.post("/feedback/")
def feedback(name: str = Form(...), ratt: int = Form(...)):
    return {
        "status": "received",
        "name": name,
        "ratting": ratt
    }


@app.post("/multiplefile/")
async def fileupla(files: List[UploadFile] = File(...)):
    result = []

    for file in files:
        content = await file.read()

        try:
            text_p = content.decode("utf-8")[:200]
        except Exception:
            text_p = "cant open"

        result.append({
            "filename": file.filename,
            "filecontent": file.content_type,
            "filelen": len(content),
            "text": text_p
        })

    return result


@app.post("/singlefile/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = content.decode("utf-8")
    except Exception:
        text = "cant open"

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "length": len(content),
        "text": text[:200]
    }


@app.post("/multifiles/")
async def multifiles(files: List[UploadFile] = File(...)):
    result = []
    for file in files:
        content = await file.read()

        result.append({
            "filename": file.filename,
            "filetype": file.content_type,
            "length": len(content)
        })

    return result



