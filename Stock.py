import sys
from regression import exponentialRegression
import matplotlib.pyplot as plt
import time
import requests
import keys
import numpy as np

class Stock:

    def __init__(self, data):
        for datum in data:
            setattr(self, datum, data[datum])
        self.symbol = self.symbol.rstrip()

    def findClosingPrices(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}".format(self.symbol.replace(".","%2E"), keys.alphavantageKey)
        try:
            res = requests.get(url).json()
            dates = res["Time Series (Daily)"]
        except:
            if "Note" in res.keys():
                raise Exception("no more api calls")
            raise Exception(res)
        closingPrices = []
        self.firstDate = list(dates.keys())[-1]
        self.lastDate = list(dates.keys())[0]
        for date in dates:
            closingPrices.insert(0, float(dates[date]["4. close"]))
        self.closingPrices = closingPrices
        print("{} prices obtained".format(self.symbol))
        time.sleep(12)

    def findRegressionValues(self): # 252 trading days each year
        self.full = exponentialRegression(self.closingPrices)
        self.last20 = exponentialRegression(self.closingPrices[-5040:])
        self.last10 = exponentialRegression(self.closingPrices[-2520:])
        self.last5 = exponentialRegression(self.closingPrices[-1260:])
        self.last1 = exponentialRegression(self.closingPrices[-252:])
        self.last6Months = exponentialRegression(self.closingPrices[-126:])

    def generatePlot(self):
        self.renderAndSavePlot(0, self.full, "max") # special case
        self.renderAndSavePlot(5040, self.last20, "20y")
        self.renderAndSavePlot(2520, self.last10, "10y")
        self.renderAndSavePlot(1260, self.last5, "5y")
        self.renderAndSavePlot(252, self.last1, "12m")
        self.renderAndSavePlot(126, self.last6Months, "6m")

    def renderAndSavePlot(self, size, timeSeries, name):
        prices = self.closingPrices[(-1 * size):]
        if size == 0:
            prices = self.closingPrices
        fig= plt.figure(figsize=(2.8,1.3))
        plt.plot(prices, linewidth=1)
        x = np.arange(len(prices))
        y = np.multiply(np.power((timeSeries["roi"] / 100 + 1), (x / 252)), timeSeries["scalar"])
        plt.plot(y)
        plt.xticks([])
        plt.yticks([])
        plt.box(on=None)
        plt.savefig('images/{}_{}.png'.format(self.symbol.lower(), name), transparent = False, bbox_inches = 'tight', pad_inches = 0)
        plt.clf()
        plt.cla()
        plt.close()

    def getRow(self):
        return (self.symbol, self.company, self.sector, self.industry, self.full["roi"], self.last20["roi"], self.last10["roi"], self.last5["roi"],self.last1["roi"], self.last6Months["roi"],  self.full["r2"], self.last20["r2"], self.last10["r2"], self.last5["r2"], self.last1["r2"], self.last6Months["r2"], self.firstDate, self.lastDate)

    def getDict(self):
        return {
            "symbol": self.symbol,
            "company": self.company,
            "sector": self.sector,
            "industry": self.industry,
            "max": self.full,
            "20y": self.last20,
            "10y": self.last10,
            "5y": self.last5,
            "12m": self.last1,
            "6m": self.last6Months,
            "firstDate": self.firstDate,
            "lastDate": self.lastDate
        }
