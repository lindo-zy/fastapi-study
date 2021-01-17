#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get('/')
def index():
    return {'hello': 'world'}


@app.get('/item/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}


def start():
    uvicorn.run(app='app:app', reload=True, debug=True)


if __name__ == '__main__':
    start()
