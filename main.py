from Stock import Stock
from finsymbols import symbols
import xlsxwriter

workbook = xlsxwriter.Workbook('test2.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.write(0, 0, "Symbol", bold)
worksheet.write(0, 1, "Company", bold)
worksheet.write(0, 2, "Sector", bold)
worksheet.write(0, 3, "Industry", bold)
# worksheet.write(0, 4, "Yearly Gain", bold)
worksheet.write(0, 4, "Growth Rate", bold)
worksheet.write(0, 5, "R^2", bold)
worksheet.write(0, 6, "Chart", bold)
worksheet.write(0, 7, "Closing Prices", bold)

companies = symbols.get_sp500_symbols()[0:5]

for i, company in enumerate(companies):
    stock = Stock(company)
    stock.findClosingPrices()
    stock.findRegressionValues()
    worksheet.write(i + 1, 0, stock.symbol)
    worksheet.write(i + 1, 1, stock.company)
    worksheet.write(i + 1, 2, stock.sector)
    worksheet.write(i + 1, 3, stock.industry)
    # worksheet.write(i + 1, 4, stock.scalar * stock.base)
    worksheet.write(i + 1, 4, stock.base)
    worksheet.write(i + 1, 5, stock.rSquared)
    worksheet.write(i + 1, 6, "this will be a chart")
    # for j, price in enumerate(stock.closingPrices):
    #     worksheet.write(i + 1, 7 + j, price)
workbook.close()
# keys = list(stock.__dict__.keys())
# for col, key in enumerate(keys):
#     # print(getattr(stock, key))
#     try:
#         worksheet.write(i, col, getattr(stock, key))
#     except TypeError:
#         worksheet.write(i, col, str(getattr(stock, key)))
