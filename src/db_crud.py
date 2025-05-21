import sqlite3

conn = sqlite3.connect("api_database.db")

creat_table_query = '''create table if not exists api
                        (id integer primary key autoincrement,
                        item text
                        )'''

cursor = conn.cursor()
cursor.execute(creat_table_query)

conn.commit()
conn.close()

def create(item):
    conn = sqlite3.connect("api_database.db")
    cursor = conn.cursor()
    cursor.execute('insert into api (item) values (?)', (item,))
    conn.commit()
    conn.close()

def read_all(column = '*'):
    conn = sqlite3.connect("api_database.db")
    cursor = conn.cursor()
    cursor.execute(f"select {column} from api")
    All = cursor.fetchall()
    conn.close()
    if column != '*':
        All_new = []
        for i in range(len(All)):
            All_new.append(All[i][0])
        return All_new
    else:
        return All

def read_i(id):
    conn = sqlite3.connect("api_database.db")
    cursor = conn.cursor()
    cursor.execute("select * from api where id = ?", (id,))
    item = cursor.fetchone()
    conn.close()
    return item

def update(item, id):
    conn = sqlite3.connect("api_database.db")
    cursor = conn.cursor()
    cursor.execute("update api set item = ? where id = ?", (item, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("api_database.db")
    cursor = conn.cursor()
    cursor.execute("delete from api where id = ?", (id,))
    conn.commit()
    conn.close()