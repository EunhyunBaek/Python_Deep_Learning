# coding=utf-8
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

class Hyun_Regression_Analysis:
    X_train = np.array([[10], [20], [30], [50]])
    y_train = np.array([[25], [45], [65], [105]])
    model = LinearRegression(fit_intercept=True)  # 상수항이 있으면
    model.fit(X_train, y_train)
    X_test = 40
    y_predict = model.predict(X_test)
    y_pred = model.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)
    w1 = model.coef_
    w0 = model.intercept_
    def predict(x):
        return Hyun_Regression_Analysis.w0 + Hyun_Regression_Analysis.w1 * x
    def Print(self):
        print(Hyun_Regression_Analysis.mse)
        print("가중치: ", Hyun_Regression_Analysis.model.coef_)
        print("상수 : ", Hyun_Regression_Analysis.model.intercept_)
        print("예상 값 :", " x 값 :", Hyun_Regression_Analysis.X_test, " y_predict :", Hyun_Regression_Analysis.y_predict)
    def Draw_Grap(self):
        x_new = np.arange(0, 51)
        y_new1 = Hyun_Regression_Analysis.predict(x_new)
        y_new = y_new1.reshape(-1, 1)

        plt.scatter(Hyun_Regression_Analysis.X_train, Hyun_Regression_Analysis.y_train, label="data")
        plt.plot(x_new, y_new, 'r-', label="regression")
        plt.scatter(Hyun_Regression_Analysis.X_test, Hyun_Regression_Analysis.y_predict, label="predict")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Linear Regression with sckit_learn")
        plt.legend()
        plt.show()

hyun = Hyun_Regression_Analysis
hyun.Print(0)
hyun.Draw_Grap(0)