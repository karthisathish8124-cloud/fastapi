
import sqlite3


con = sqlite3.connect("items.db", check_same_thread=False)
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        des TEXT
    )
""")
con.commit()