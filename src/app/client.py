import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI
from sqlalchemy import select, desc, true

from src.db.connection import init_db, SyncSession
from src.app.fetcher import async_get_and_save_tickers_data
from src.db.models import TickerData


def iso_to_timestamp(iso_date: str) -> int:
    dt = datetime.fromisoformat(iso_date)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    return int(dt.timestamp())


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI()


@app.get('/fetch_ticker')
def fetch_ticker():
    asyncio.run(async_get_and_save_tickers_data(['BTC-PERPETUAL']))
    return {'asdf0': 'asdf'}


@app.get('/get_all_currency_data')
def get_all_currency_data(ticker: str):
    with SyncSession() as db_session:
        query = (
            select(TickerData)
            .where(TickerData.ticker == ticker)
        )
        return db_session.scalars(query).all()


@app.get('/get_last_currency_price')
def get_last_currency_price(ticker: str):
    with SyncSession() as db_session:
        query = (
            select(TickerData)
            .where(TickerData.ticker == ticker)
            .order_by(desc(TickerData.timestamp))
            .limit(1)
        )
        ticker_data = db_session.scalars(query).first()
        return ticker_data.btc_usd if ticker_data else None


@app.get('/get_currency_price')
def get_currency_price(ticker: str, start_iso_date: str = None, end_iso_date: str = None):
    with SyncSession() as db_session:
        query = (
            select(TickerData)
            .where(
                TickerData.ticker == ticker,
                TickerData.timestamp >= iso_to_timestamp(start_iso_date) if start_iso_date else true(),
                TickerData.timestamp >= iso_to_timestamp(end_iso_date)   if end_iso_date   else true(),
            )
        )

        return db_session.scalars(query).all()