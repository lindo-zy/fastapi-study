#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post('/items/q')
def create_item(item: Item, q: Optional[str] = Query(..., max_length=3)):
    if q:
        print(q)
    return item


@app.get('/items/')
def read_item(q: Optional[List[str]] = Query(None, deprecated=True)):
    query_item = {'q': q}
    return query_item


def run():
    uvicorn.run(app='main:app', reload=True, debug=True)


if __name__ == '__main__':
    run()
