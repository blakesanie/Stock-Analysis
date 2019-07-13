import numpy as np
from sklearn.linear_model import LinearRegression
# from scipy.optimize import curve_fit

# x = np.arange(1,7).reshape((-1, 1))
# y = np.log([1, 1.5, 3, 6, 10, 15])
#
# model = LinearRegression()
#
# model.fit(x, y)
#
# r_sq = model.score(x, y)
# a = np.exp(model.intercept_)
# b = np.exp(model.coef_)[0]
# print("y ~ {}*{}^x".format(a,b))

def exponentialRegression(closing):
    x = np.arange(1,len(closing) + 1).reshape((-1, 1))
    y_normalized = np.divide(closing, closing[0])
    y_ln = np.log(y_normalized)
    model = LinearRegression()
    model.fit(x, y_ln)
    return (np.exp(model.intercept_), np.power(np.exp(model.coef_)[0], 365.25), model.score(x, y_ln))
