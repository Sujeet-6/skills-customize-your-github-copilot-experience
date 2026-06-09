from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory "database"
items: Dict[int, Item] = {}


@app.get("/items")
def list_items():
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item id already exists")
    items[item.id] = item
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
