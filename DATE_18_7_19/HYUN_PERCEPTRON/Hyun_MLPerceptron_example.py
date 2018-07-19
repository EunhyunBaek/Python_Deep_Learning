# coding=utf-8
from sklearn.neural_network import MLPClassifier
class Hyun_MLPerceptron:
    mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    #mlp.fit(X_train, y_test)
    def Get_mlp(self):
        return Hyun_MLPerceptron.mlp
    def Train_mlp(self):
        mlp=Hyun_MLPerceptron.Get_mlp(0)
        X_train = [[0., 0.], [1., 1.]]
        y_test = [0, 1]
        mlp.fit(X_train, y_test)
        return mlp
    def Print(self):
        mlp=Hyun_MLPerceptron.Train_mlp(0)
        new_data = [[2., 2.], [-1., -2.]]
        print("clf.predict([[2., 2.], [-1., -2.]] :", mlp.predict(new_data))
        print("mlp.coefs_ :", mlp.coefs_)
        print("coef.shape :", [coef.shape for coef in mlp.coefs_])
        print("mlp.n_outputs_ : ", mlp.n_outputs_)
        print("mlp.classes_:", mlp.classes_)
        # MLPClassifier supports only the Cross-Entropy loss function,
        # which allows probability estimates by running the predict_proba method.
        print("self._label_binarizer.y_type_ :", mlp._label_binarizer.y_type_)
        # softmax
        print("clf.predict_proba([[2., 2.], [1., 2.]] :", mlp.predict_proba([[2., 2.], [1., 2.]]))
        print("n_outputs_ : ", mlp.n_outputs_)

hyun = Hyun_MLPerceptron
hyun.Print(0)