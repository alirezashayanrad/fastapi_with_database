from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"output" : "api"}

item_list = []
@app.post('/items/<newitem>')
def insert_item(newitem):
    item_list.append(newitem)
    return item_list

@app.get('/items/{index}')
def get_item(index):
    index_i = int(index)
    if index_i >= 0 and index_i < len(item_list):
        return item_list[index_i]
    else:
        return 'You Entered out of range'

@app.get('/lastitems/last')
def get_last():
    return item_list[-1]

@app.get('/firstitems/first')
def get_first():
    return item_list[0]