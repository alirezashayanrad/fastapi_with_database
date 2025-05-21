from fastapi import FastAPI
import db_crud

app = FastAPI()

@app.get('/')
def home():
    return {"output" : "api"}

@app.post('/create_item/<newitem>')
def create_item(newitem):
    db_crud.create(newitem)
    return "saved"

@app.get('/r_all_item/{column}')
def read_all_item(column):
    return db_crud.read_all(column)

@app.get('/r_item/{read_index}')
def read_item(read_index):
    index_i = int(read_index)
    if index_i in db_crud.read_all("id"):
        return db_crud.read_i(index_i)
    
    else:
        return "out of range"
    
@app.post('/update_item/<update_item>/<index>')
def update(update_item, update_index):
    index_i = int(update_index)
    if index_i in db_crud.read_all("id"):
        db_crud.update(update_item, index_i)
        return "updated"
    
    else:
        return "out of range"
    
@app.post('/delete_item/<delete_index>')
def delete(delete_index):
    index_i = int(delete_index)
    if index_i in db_crud.read_all("id"):
        db_crud.delete(index_i)
        return "deleted"
    
    else:
        return "out of range"