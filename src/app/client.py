import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db.connection import init_db
from src.app.fetcher import fetch_tickers_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/fetch_ticker")
def fetch_ticker(ticker: str):
    asyncio.run(fetch_tickers_data('BTC-PERPETUAL'))
    return {'asdf0': 'asdf'}


@app.get("/all_currency_data")
def all_currency_data(ticker: str):
    return {'asdf1': 'asdf'}


@app.get("/get_last_currency_price")
def get_last_currency_price(ticker: str):
    return {'asdf2': 'asdf'}


@app.get("/get_last_currency_price")
def get_currency_price(ticker: str, date):
    return {'asdf3': 'asdf'}