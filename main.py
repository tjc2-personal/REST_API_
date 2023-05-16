from fastapi import FastAPI
from model import Item
from datetime import datetime, timezone
from uuid import uuid4

db = {}

app = FastAPI()

@app.post("/item", response_model=Item)
def post_item(item_data: dict):
    """
    Endpoint: given a JSON payload that follows the form, {"Label":"Value"} add a new entry to the database
    and return the ID, label data, and the time stamp
    :param item_data: Dictionary describing the item {"Label":"Value"}
    :return: Item-type from model.py
    """
    item_id = uuid4().hex
    item = Item(id=item_id, label=item_data["label"], create_ts=datetime.now(timezone.utc))
    db[item_id] = item
    return item

@app.get("/item/all", response_model=list[Item])
def get_all_items():
    return list(db.values())

@app.get("/item/{id}", response_model=Item)
def get_item(id: str):
    item = db.get(id)
    if item:
        return item
    else:
        return {"error": "There exists no item which can be referenced based on the supplied ID."}

