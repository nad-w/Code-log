
tickers = {
    "AAPL": "Apple Inc",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Google",
    "AMZN": "Amazon",
    "TSLA": "Tesla",
}

print("symbol  |  company")
print("-------------------")

for symbol, company in tickers.items():
     print(f"{symbol:<6}  | {company}")