from Stock import Stock
from finsymbols import symbols
import csv
import os

companies = symbols.get_sp500_symbols()[0:2]

with open('SP500StockData.csv', 'w') as output:
    writer = csv.writer(output)
    writer.writerow(("Symbol","Company","Sector","Industry","Exp. Regression Equation","Annual Return (%)","R^2","First Date","Last Date"))
    for i, company in enumerate(companies):
        stock = Stock(company)
        stock.findClosingPrices()
        stock.findRegressionValues()
        writer.writerow(stock.getRow())

output.close()
os.system("open SP500StockData.csv")
