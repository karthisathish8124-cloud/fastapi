from fastapi.openapi.utils import status_code_ranges
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database setup
con = sqlite3.connect("test.db", check_same_thread=False)
cursor = con.cursor()

# Ensure table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        des TEXT
    )
""")
con.commit()

class item(BaseModel):
    name: str
    des: str

@app.post("/create/item")
def create_item(i: item):
    try:
        cursor.execute("INSERT INTO items (name, des) VALUES (?, ?)", (i.name, i.des))
        con.commit()
        return {"message": "item stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"invalid input: {e}")

@app.get("/read/items")
def read():
    try:
        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()
        return [{"id": r[0], "name": r[1], "des": r[2]} for r in rows]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"unable to read: {e}")


@app.get("/read1/{name}")
def read1(name: str):
    try:
        cursor.execute("SELECT * FROM items WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="invalid name")
        return {"id": row[0], "name": row[1], "des": row[2]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"unable to read: {e}")

@app.put("/item/update")
def update(id:int,i:item):
    try:
        cursor.execute("update items set name=?,des=? where id = ?",(i.name,i.des,id))
        con.commit()
        return{"message":"items updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"unable to update: {e}")

@app.delete("/item/delete")
def delete(id: int):
    try:
        cursor.execute("DELETE FROM items WHERE id = ?", (id,))
        con.commit()
        return {"message": "items deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"unable to delete: {e}")