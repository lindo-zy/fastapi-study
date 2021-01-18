#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
def read_items(item_id: int = None, q: Optional[str] = Query(
    None, alias='q2'
)):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


# @app.get('/items/{item_id}')
# def read_items(item_id: int = Path(..., title='The ID'), q: Optional[str] = Query(
#     None, alias='item_query'
# )):
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results

def run():
    uvicorn.run(app='main:app', reload=True, debug=True)


if __name__ == '__main__':
    run()
