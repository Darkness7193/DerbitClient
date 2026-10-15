import requests
import uvicorn


def get_public_ticker(instrument_name: str):
    url = 'https://test.deribit.com/api/v2/public/ticker'

    payload = {
        'jsonrpc': '2.0',
        'id': 8106,
        'method': 'public/ticker',
        'params': {'instrument_name': instrument_name}
    }
    headers = {'Content-Type': 'application/json'}

    return requests.post(url, json=payload, headers=headers).json()['result']


if __name__ == '__main__':
    print(get_public_ticker('BTC-PERPETUAL'))
    uvicorn.run('src.app.client:app', host='0.0.0.0', port=8000, reload=True)