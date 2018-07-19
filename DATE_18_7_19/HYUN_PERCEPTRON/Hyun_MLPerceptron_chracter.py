# coding=utf-8
from sklearn.neural_network import MLPClassifier
from sklearn    import datasets
import matplotlib.pyplot   as plt
class Hyun_MLPerceptron_Charcter:
    digits = []
    X_train, y_train = [], []
    def Load_Data(self):
        digits=Hyun_MLPerceptron_Charcter.digits = datasets.load_digits()
        Hyun_MLPerceptron_Charcter.X_train, Hyun_MLPerceptron_Charcter.y_train = digits.data[:-10], digits.target[:-10]
        Hyun_MLPerceptron_Charcter.X_train, Hyun_MLPerceptron_Charcter.y_train = digits.data[:-10], digits.target[:-10]
    def Get_TrainData(self):
        return Hyun_MLPerceptron_Charcter.X_train,Hyun_MLPerceptron_Charcter.y_train
    def Train_Data(self):
        mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10, 10, 10), max_iter=1000, alpha=1e-4,
                            # mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, alpha=1e-4,
                            solver='sgd', verbose=10, tol=1e-4, random_state=1,
                            learning_rate_init=.001)
        X_train , y_train = Hyun_MLPerceptron_Charcter.Get_TrainData(0)
        mlp.fit(X_train, y_train)
        return mlp
    def Get_digits(self):
        return Hyun_MLPerceptron_Charcter.digits
    def Get_digits_index(self):
        return 9
    def Get_TestData(self):
        digits=Hyun_MLPerceptron_Charcter.Get_digits(0)
        digits_index = Hyun_MLPerceptron_Charcter.Get_digits_index(0)
        x_test = digits.data[digits_index].reshape(1, -1)
        return x_test
    def Draw_Grap(self):
        Hyun_MLPerceptron_Charcter.Load_Data(0)
        x_test=Hyun_MLPerceptron_Charcter.Get_TestData(0)
        digits=Hyun_MLPerceptron_Charcter.Get_digits(0)
        digits_index=Hyun_MLPerceptron_Charcter.Get_digits_index(0)
        mlp = Hyun_MLPerceptron_Charcter.Train_Data(0)
        print(mlp.predict(x_test))
        # print('Test accuracy:', mlp.score(X_test, y_test))
        plt.imshow(digits.images[digits_index], cmap=plt.cm.gray_r, interpolation='nearest')
        plt.show()
hyun =Hyun_MLPerceptron_Charcter
hyun.Draw_Grap(0)
