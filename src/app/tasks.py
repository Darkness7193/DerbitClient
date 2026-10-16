import asyncio
from decimal import Decimal
from uuid import uuid4

import aiohttp

from src.db.models import TickerData
from src.db.connection import AsyncSession
from src.celery_app import celery_app


async def async_get_public_ticker(http_session: aiohttp.ClientSession, instrument_name: str):
    url = 'https://test.deribit.com/api/v2/public/ticker'

    payload = {
        'jsonrpc': '2.0',
        'id': uuid4().int,
        'method': 'public/ticker',
        'params': {'instrument_name': instrument_name}
    }
    headers = {'Content-Type': 'application/json'}

    async with http_session.post(url, json=payload, headers=headers) as response:
        response.raise_for_status()
        return (await response.json())['result']


async def async_get_and_save_tickers_data(instruments_names: list[str]):
    async with aiohttp.ClientSession() as http_session:
        calls = [
            async_get_public_ticker(http_session, instrument_name)
            for instrument_name in instruments_names
        ]

        results = await asyncio.gather(*calls)

        tickers_data_objs = [
            TickerData(
                ticker=   result['instrument_name'],
                btc_usd=  Decimal(str(result['last_price'])),
                eth_usd=  Decimal(str(result['index_price'])),
                timestamp=result['timestamp'] // 1000,
            )
            for result in results
        ]

        async with AsyncSession() as db_session:
            db_session.add_all(tickers_data_objs)
            await db_session.commit()


@celery_app.task(name='fetch_and_save_tickers')
def fetch_and_save_tickers():
    print('task task task')
    asyncio.run(
        async_get_and_save_tickers_data([
            'BTC-PERPETUAL'
        ])
    )