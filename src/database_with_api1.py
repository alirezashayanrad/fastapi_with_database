from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get('/')
def home():
    return {"output" : "api"}

conn = sqlite3.connect("api_database.db")

creat_table_query = '''create table if not exists api
                        (id integer primary key autoincrement,
                        number text
                        )'''

cursor = conn.cursor()
cursor.execute(creat_table_query)

conn.commit()

def create(item):
    cursor.execute('insert into api (item) values (?)', (item,))
    conn.commit()

@app.post('/items/<newitem>')
def save_number(newitem):
    create(str(newitem))
    return "done"