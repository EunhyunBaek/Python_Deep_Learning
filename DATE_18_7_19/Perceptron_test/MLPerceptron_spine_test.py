import numpy as np
import pandas as pd

from subprocess import check_output
#print(check_output([\"ls\", \"../input\"]).decode(\"utf8\"))

import matplotlib.pyplot as plt


import seaborn as sns
df = pd.read_csv('d:/ML/data/Dataset_spine.csv')

df = df.drop(['Unnamed: 13'], axis=1)

print(df.head())
print(df.describe())

df = df.drop(['Col7','Col8','Col9','Col10','Col11','Col12'], axis=1)
print(df.head())

from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# abnormal, normal
y = df['Class_att']
# 310 데이터
print('y :', y[0])

x = df.drop(['Class_att'], axis=1)

#print('y :', y)

# DataFramee, Series 타입으로 리턴됨.
# x_train(232x6), y_train(232,), x_test(78,6), y_test(78,)
x_train, x_test, y_train, y_test = [], [], [], []
print("x_test :", x_test.shape)
print('y_train :', y_train[0])
clf =  MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, alpha=0.0001,
                    solver='sgd', verbose=10,  random_state=21,tol=0.000000001)
# verbose 가 하는 역할 : 콘솔 아웃풋 지정
# alpha : L2 penalty (regularization term) parameter
#clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=500, alpha=0.0001,
#                    solver='sgd', verbose=10,  random_state=21,tol=0.000000001)
'''
print('x_train  shape', x_train.shape, 'type :', type(x_train))
print('y_train  shape', y_train.shape, 'type :', type(y_train))
print('x_test  shape', x_test.shape, 'type :', type(x_test))
print('y_test  shape', y_test.shape, 'type :', type(y_test))
'''
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
accuracy_score(y_test, y_pred)


cm = confusion_matrix(y_test, y_pred)
print("cm :", cm)

sns.heatmap(cm, center=True)
plt.show()