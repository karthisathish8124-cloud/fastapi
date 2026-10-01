from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

con = sqlite3.connect("test.db", check_same_thread=False)
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        des TEXT
    )
""")
con.commit()