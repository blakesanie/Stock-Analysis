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
        self.firstDate = list(dates.keys())[-1]
        self.lastDate = list(dates.keys())[0]
        for date in dates:
            closingPrices.insert(0, float(dates[date]["4. close"]))
        self.closingPrices = closingPrices
        print("{} prices obtained".format(self.symbol))
        time.sleep(12)

    def findRegressionValues(self):
        values = exponentialRegression(self.closingPrices)
        self.scalar = values["scalar"]
        self.base = values["base"]
        self.annualReturn = values["annualReturn"]
        self.rSquared = values["rSquared"]
        self.equation = values["equation"]

    def getRow(self):
        return (self.symbol, self.company, self.sector, self.industry, self.equation, self.annualReturn, self.rSquared, self.firstDate, self.lastDate)
