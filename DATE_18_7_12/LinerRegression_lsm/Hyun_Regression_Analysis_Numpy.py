# coding=utf-8
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

class Hyun_Regression_Analysis:
    y_predict=[]
    X_test=0
    X1 = np.array([[10], [20], [30], [50]])
    y_label = np.array([[25], [45], [65], [105]])
    X_train = sm.add_constant(X1)  # 오그멘테이션
    w = np.dot(np.dot(np.linalg.inv(np.dot(X_train.T, X_train)), X_train.T), y_label)
    w0, w1 = w[0],w[1]
    def predict(x):
        return Hyun_Regression_Analysis.w0 + Hyun_Regression_Analysis.w1* x
    def Print(self):
        Hyun_Regression_Analysis.X_test = 40
        Hyun_Regression_Analysis.y_predict = Hyun_Regression_Analysis.predict(Hyun_Regression_Analysis.X_test)
        print(Hyun_Regression_Analysis.X1)
        print("가중치: ", Hyun_Regression_Analysis.w1)
        print("상수 : ", Hyun_Regression_Analysis.w0)
        print("예상 값 :", " x 값 :", Hyun_Regression_Analysis.X_test, " y_predict :", Hyun_Regression_Analysis.y_predict)
        temp = np.dot(np.linalg.inv(np.dot(Hyun_Regression_Analysis.X_train.T,Hyun_Regression_Analysis.X_train)),Hyun_Regression_Analysis.X_train.T)
        print(temp.shape)
        print(Hyun_Regression_Analysis.w.shape)
    def Draw_Grap(self):
        x_new = np.arange(0, 51)
        y_new = Hyun_Regression_Analysis.predict(x_new)

        print(x_new)
        print(y_new)

        plt.scatter(Hyun_Regression_Analysis.X1,Hyun_Regression_Analysis.y_label, label="data")
        plt.scatter(Hyun_Regression_Analysis.X_test,Hyun_Regression_Analysis.y_predict, label="predict")
        plt.plot(x_new, y_new, 'r-', label="regression")
        plt.xlabel("House Size")
        plt.ylabel("House Price")
        plt.title("Linear Regression _ with numpy")
        plt.legend()
        plt.show()

hyun=Hyun_Regression_Analysis
hyun.Print(0)
hyun.Draw_Grap(0)

