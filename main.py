import asyncio
import uvicorn

from app.fetcher import get_public_ticker


if __name__ == '__main__':
    print(asyncio.run(get_public_ticker('BTC-PERPETUAL')))
    uvicorn.run('src.app.client:app', host='0.0.0.0', port=8000, reload=True)