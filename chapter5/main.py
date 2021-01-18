#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


# @app.put("/items/{item_id}")
# async def update_item(
#         item_id: int, item: Item, user: User, importance: int = Body(...)
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results


@app.put("/items/{item_id}/{importance}")
def update_item(
        item_id: int, item: Item, user: User, importance: int
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


def run():
    uvicorn.run(app='main:app', reload=True, debug=True)


if __name__ == '__main__':
    run()
