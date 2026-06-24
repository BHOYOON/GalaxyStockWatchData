import json
import yfinance as yf

ticker = yf.Ticker("005930.KS")

price = ticker.history(period="1d")

close = int(price["Close"].iloc[-1])

result = {
    "name": "SAMSUNG",
    "price": f"{close:,}",
    "change": "LIVE",
    "time": "AUTO"
}

with open("price.json", "w") as f:
    json.dump(result, f, indent=2)
