import requests

from fastapi import FastAPI


app = FastAPI()


@app.get("/all_currency_data")
def all_currency_data(ticker: str):
    return {'asdf1': 'asdf'}


@app.get("/get_last_currency_price")
def get_last_currency_price(ticker: str):
    return {'asdf2': 'asdf'}


@app.get("/get_last_currency_price")
def get_currency_price(ticker: str, date):
    return {'asdf3': 'asdf'}