import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import select

from src.db.connection import init_db, SyncSession
from src.app.fetcher import async_get_and_save_tickers_data
from src.db.models import TickerData


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI()


@app.get('/fetch_ticker')
def fetch_ticker():
    asyncio.run(async_get_and_save_tickers_data(['BTC-PERPETUAL']))
    return {'asdf0': 'asdf'}


@app.get('/all_currency_data')
def all_currency_data(ticker: str):
    with SyncSession() as db_session:
        query = select(TickerData).where(TickerData.ticker == ticker)
        return db_session.scalars(query).all()


@app.get('/get_last_currency_price')
def get_last_currency_price(ticker: str):
    return {'asdf2': 'asdf'}


@app.get('/get_last_currency_price')
def get_currency_price(ticker: str, date):
    return {'asdf3': 'asdf'}