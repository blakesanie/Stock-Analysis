from finsymbols import symbols
import requests
import time

data = symbols.get_sp500_symbols()[0:10] # so we dont overflow the api

for i, stock in enumerate(data):
    symbol = stock["symbol"].rstrip()
    try:
        res = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey=Q89RW8U7CR3LC2AL".format(symbol)).json()
        dates = res["Time Series (Daily)"]
    except:
        print(res)
        break
    closingPrices = []
    for date in dates:
        closingPrices.insert(0, float(dates[date]["4. close"]))
    stock["closingPrices"] = closingPrices
    print("{} of 500 done".format(i + 1))
    time.sleep(12)

print(data)
# av = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SQ&outputsize=full&apikey=Q89RW8U7CR3LC2AL").json()
#
# for date in av["Time Series (Daily)"]:
#     print(av["Time Series (Daily)"][date]["4. close"])
