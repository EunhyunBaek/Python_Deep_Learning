'''
필기체 인식을 위한 다층 신경망 모델 적용

'''


from sklearn.neural_network import MLPClassifier
from sklearn import datasets
import matplotlib.pyplot as plt


digits = datasets.load_digits()
X_train,y_train = digits.data[:-10], digits.target[:-10]
X_train,y_train = digits.data[:-10], digits.target[:-10]

#  히든 1개 (50 ) : 손실 : 0.01946
#  히든 5층(10, 10, 10, 10, 10 ) : 손실 :0.11663753
#   로스가 더이상 줄지 않으면 scikit_learn에서 알아서 멈춰준다..
# 내부적으로 early stop과는 다른 로직으로 처리 됨.
# (sckit-learn에서는 내부적으로 10% 의 훈련 데이터를 가지고 early stop 구현
mlp = MLPClassifier(hidden_layer_sizes=(10,10, 10, 10, 10), max_iter=1000, alpha=1e-4,
#mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                   learning_rate_init=.001)

mlp.fit(X_train, y_train)

#print('Train accuracy:', mlp.score(X_train, X_train))

digits_index = 9

x_test = digits.data[digits_index].reshape(1,-1)

print(mlp.predict(x_test))
#print('Test accuracy:', mlp.score(X_test, y_test))
plt.imshow(digits.images[digits_index], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()