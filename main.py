from Stock import Stock
from finsymbols import symbols
import csv
import os
import json

companies = symbols.get_sp500_symbols()#[0:5]
print(len(companies))

stockDicts = []

with open('SP500StockData.csv', 'w') as csvOut:
    writer = csv.writer(csvOut)
    writer.writerow(("Symbol","Company","Sector","Industry","avg. ROI (%) - Max","avg. ROI (%) - 20 Years","avg. ROI (%) - 10 Years","avg. ROI (%) - 5 Years","avg. ROI (%) - 1 Year","avg. ROI (%) - 6 Months","R^2 - Max", "R^2 - 20 Years", "R^2 - 10 Years", "R^2 - 5 Years", "R^2 - 1 Year", "R^2 - 6 Months", "First Date", "Last Date"))
    for i, company in enumerate(companies):
        stock = Stock(company)
        try:
            stock.findClosingPrices()
        except Exception as e:
            print(str(e))
            if not str(e) == "no more api calls":
                continue
            else:
                break
        stock.findRegressionValues()
        writer.writerow(stock.getRow())
        stockDicts.append(stock.getDict())

csvOut.close()
with open('data.json', 'w') as jsonOut:
    json.dump(stockDicts, jsonOut)

jsonOut.close()
