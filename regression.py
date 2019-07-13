import numpy as np
from sklearn.linear_model import LinearRegression

def exponentialRegression(closing):
    x = np.arange(1,len(closing) + 1).reshape((-1, 1))
    y_normalized = np.divide(closing, closing[0])
    y_ln = np.log(y_normalized)
    model = LinearRegression()
    model.fit(x, y_ln)
    scalar = np.exp(model.intercept_) * closing[0]
    base = np.exp(model.coef_)[0]
    annualReturn = (np.power(np.exp(model.coef_)[0], 365.25) - 1) * 100
    equation = "y = {} * {}^x + {}".format(scalar, base, closing[0])
    rSquared = model.score(x, y_ln)
    return {
        "scalar": scalar,
        "base": base,
        "annualReturn": annualReturn,
        "equation": equation,
        "rSquared": rSquared
    }
