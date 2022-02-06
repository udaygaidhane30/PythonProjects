import requests

API_KEY = "K9662R3WTX8DYY12"
API_ADD = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "interval": "5min",
    "symbol": "RELIANCE.BSE",
    "apikey": API_KEY,
}

response = requests.get(url=API_ADD, params=parameters)
response.raise_for_status()
stock_data = response.json()
print(stock_data)
