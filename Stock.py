import sys
from regression import exponentialRegression
import time
import requests
import keys

class Stock:

    def __init__(self, data):
        for datum in data:
            setattr(self, datum, data[datum])
        self.symbol = self.symbol.rstrip()
    def findClosingPrices(self):
        # self.closingPrices = [2,3,4,6,8,12,18]
        try:
            res = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}".format(self.symbol, keys.alphavantageKey)).json()
            dates = res["Time Series (Daily)"]
        except:
            sys.exit(res)
        closingPrices = []
        for date in dates:
            closingPrices.insert(0, float(dates[date]["4. close"]))
        self.closingPrices = closingPrices
        print("{} prices obtained".format(self.symbol))
        time.sleep(12)
    def findRegressionValues(self):
        values = exponentialRegression(self.closingPrices)
        self.scalar = values[0]
        self.base = values[1]
        self.rSquared = values[2]
    def getStockData(self):
        print(self)
