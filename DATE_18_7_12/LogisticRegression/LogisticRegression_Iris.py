# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:10:19 2017

@author: BEAST
"""

# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
# import some data to play with
iris = datasets.load_iris()
print(iris)
# iris 데이터 중 꽃 받침의 길이와 너비의 데이터만 사용
X_train = iris.data[:, :2]  # we only take the first two features.
y_train = iris.target

print('y_train :', y_train)
# sepal : 꽃 받침   petal : 꽃임
#  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 데이터의 구성 확인

#print(iris.feature_names)

# 컬러 그림을 그리기위한 격자 크기 설정
h = .02  # step size in the mesh

# 로지스틱 회귀 분석 모델 생성 및 학습
logreg = LogisticRegression(C=1e5)
logreg.fit(X_train, y_train)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
# 꽃 받침 길이
x_min, x_max = X_train[:, 0].min() - .5, X_train[:, 0].max() + .5
# 꽃 받침 넓이
y_min, y_max = X_train[:, 1].min() - .5, X_train[:, 1].max() + .5

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
'''
print(xx)
print(yy)

print(xx.shape)
'''
temp = np.c_[xx.ravel(), yy.ravel()]
'''
print(temp[:,0])
print(temp[:,1])
'''
# np.c_ : 열추가  np.r_ 행추가
# xx.ravel () --> 1 차원 배열로 변환
#Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])
Z = logreg.predict(temp)

print(Z.shape)
# Put the result into a color plot
Z = Z.reshape(xx.shape)
#plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()