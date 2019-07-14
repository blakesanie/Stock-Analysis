from Stock import Stock
from finsymbols import symbols
import csv
import os
import json

companies = symbols.get_sp500_symbols()[0:2]

stockDicts = []

with open('SP500StockData.csv', 'w') as csvOut:
    writer = csv.writer(csvOut)
    writer.writerow(("Symbol","Company","Sector","Industry","Exp. Regression Equation","Annual Return (%)","R^2","First Date","Last Date"))
    for i, company in enumerate(companies):
        stock = Stock(company)
        try:
            stock.findClosingPrices()
        except Exception as e:
            print(e)
            break
        stock.findRegressionValues()
        writer.writerow(stock.getRow())
        stockDicts.append(stock.getDict())

csvOut.close()
with open('data.json', 'w') as jsonOut:
    data = json.dumps(stockDicts, indent=4, sort_keys=True)
    json.dump(data, jsonOut)

jsonOut.close()
# os.system("open SP500StockData.csv")
