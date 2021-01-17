#!/usr/bin/python3
# -*- coding:utf-8 -*-

from enum import Enum

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resent = 'resent'
    lenet = 'lenet'


@app.get('/')
def index():
    return {'item': "主页"}


@app.get('/models/{model_name}')
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': "Deep Learnign"}
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': "leCNN"}
    return {'model_name': model_name, 'message': 'Have some'}


def run():
    uvicorn.run(app='main:app', reload=True, debug=True)


if __name__ == '__main__':
    run()
