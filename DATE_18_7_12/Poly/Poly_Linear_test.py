# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:42:10 2017

@author: BEAST
"""

# -*- coding: utf-8 -*-
from sklearn.metrics import r2_score

"""
Created on Tue Nov 21 15:35:29 2017

@author: BEAST
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def make_nl_sample():
    np.random.seed(0)
    samples_number = 50
    X = np.sort(np.random.rand(samples_number))
    y = np.sin(2 * np.pi * X) + np.random.randn(samples_number) * 0.2
    X = X[:, np.newaxis]
    return (X, y)



X_train, y_train = make_nl_sample()
model=LinearRegression().fit(X_train,y_train)
predict = model.predict(X_train)


n_degree = 3

# Polynomial regression
poly_linear_model = LinearRegression()
# 차수에 맞는 형태의 데이터 형태 변환
polynomial = PolynomialFeatures(n_degree)
X_train_transformed = polynomial.fit_transform(X_train)
poly_linear_model.fit(X_train_transformed,y_train)
pre2 = poly_linear_model.predict(X_train_transformed)
#print("X_train_transformed.shape :", X_train_transformed.shape)


'''
print(y_train)
print(predict)
print(pre2)
'''

'''
print(X_train.shape)
print(y_train.shape)
'''
linear_r2_score = r2_score(y_train,predict)
poly_r2_score = r2_score(y_train,pre2)

print("linear_r2_score :",linear_r2_score)
print("poly_r2_score :",poly_r2_score)

plt.scatter(X_train, y_train, label='Training Data')
plt.plot(X_train,predict,label="Linear Regression",color='r')
plt.plot(X_train, pre2, label='Poly Regression', color='b')
plt.legend()
plt.title("Degree : {}\n linear_r2_score : {:.2e}\n poly_r2_score : {:.2e} ".format(n_degree, linear_r2_score, poly_r2_score))
plt.show()



