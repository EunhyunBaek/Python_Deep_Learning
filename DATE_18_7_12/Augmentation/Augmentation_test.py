# coding=utf-8
import statsmodels.api as sm
import numpy as np
'''
상수항이 0이 아닌 회귀분석모형인 경우에는 수식을 간단하게 만들기 위해 다음과 같이 상수항을 독립변수에 추가한다. 
이를 바이어스 오그멘테이션(bias augmentation)이라고 한다.
'''
X1= np.array([[10],[20],[30],[50]])
X_train=sm.add_constant(X1)#오그멘테이션
print("X_train")
print(X_train)
print(X_train.shape)

#X1.shape(4,1)
print("X1.shape[0]")
print(X1.shape[0])
print("np.ones")
print(np.ones((X1.shape[0],1)))
'''
hstack 명령은 행의 수가 같은 두 개 이상의 배열을 옆으로 연결하여 열의 수가 더 많은 배열을 만든다.
 연결할 배열은 하나의 리스트에 담아야 한다.
'''
X_train1=np.hstack([np.ones((X1.shape[0],1)),X1])
print("X1")
print(X1)
print("X_train1")
print(X_train1)