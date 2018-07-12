# coding=utf-8
#getter setter 상세하게 바꿀 필요 있음.
import matplotlib.pyplot as plt
import numpy as np
class Hyun_Regression_Analysis:
    sample_data = []
    w1 = 0
    w0 = 0
    X_train_a = []
    Y_train_a = []
    X_test = 0
    y_predict = 0
    def Data(data):
        Hyun_Regression_Analysis.sample_data = data
    def Predict(x):
        return Hyun_Regression_Analysis.w0 + Hyun_Regression_Analysis.w1 * x
    def Sum_Data(self):
        X_train_a = []
        Y_train_a = []
        total_size = 0
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x_square = 0
        for row in sample_data:
            X_train = row[0]
            y_train = row[1]
            X_train_a.append(row[0])
            Y_train_a.append(row[1])
            sum_xy += X_train * y_train
            sum_x += X_train
            sum_y += y_train
            sum_x_square += X_train * X_train
            total_size += 1
        Hyun_Regression_Analysis.X_train_a= X_train_a
        Hyun_Regression_Analysis.Y_train_a = Y_train_a
        w0 = (sum_x_square * sum_y - sum_xy * sum_x) / (total_size * sum_x_square - sum_x * sum_x)
        w1 = (total_size * sum_xy - sum_x * sum_y) / (total_size * sum_x_square - sum_x * sum_x)
        Hyun_Regression_Analysis.Set_Weight(w0,w1)
    def Set_Weight(a0,a1):
        Hyun_Regression_Analysis.w0 = a0
        Hyun_Regression_Analysis.w1 = a1
    def Get_Weight(self):
        a0=Hyun_Regression_Analysis.w0
        a1=Hyun_Regression_Analysis.w1
        return a0,a1
    def Print(X_test):
        w0,w1=Hyun_Regression_Analysis.Get_Weight(0)
        Hyun_Regression_Analysis.X_test = X_test
        Hyun_Regression_Analysis.y_predict = Hyun_Regression_Analysis.Predict(X_test)
        print("가중치: ", w1)
        print("상수 : ", w0)
        print("예상 값 :", " x 값 :", X_test, " y_predict :", Hyun_Regression_Analysis.y_predict)
    def Draw_Grap(self):
        x_new = np.arange(0, 51)
        y_new = Hyun_Regression_Analysis.Predict(x_new)
        plt.scatter(Hyun_Regression_Analysis.X_train_a, Hyun_Regression_Analysis.Y_train_a, label="data")
        plt.scatter(Hyun_Regression_Analysis.X_test, Hyun_Regression_Analysis.y_predict, label="predict")
        plt.plot(x_new, y_new, 'r-', label="regression")
        plt.xlabel("House Size")
        plt.ylabel("House Price")
        plt.title("Linear Regression")
        plt.legend()
        plt.show()
sample_data = [[10, 25], [20, 45], [30, 65], [50, 105]]
hyun=Hyun_Regression_Analysis
hyun.Data(sample_data)
hyun.Sum_Data(0)
hyun.Print(40)
hyun.Draw_Grap(0)