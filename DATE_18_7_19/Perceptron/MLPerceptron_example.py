from sklearn.neural_network import MLPClassifier
X_train = [[0., 0.], [1., 1.]]
y_test = [0, 1]
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
new_data = [[2., 2.], [-1., -2.]]
mlp.fit(X_train, y_test)

print("clf.predict([[2., 2.], [-1., -2.]] :", mlp.predict(new_data))
print(mlp.coefs_)
print([coef.shape for coef in mlp.coefs_])
print("mlp.n_outputs_ : ", mlp.n_outputs_)
print("mlp.classes_:", mlp.classes_)
#MLPClassifier supports only the Cross-Entropy loss function,
# which allows probability estimates by running the predict_proba method.
print("self._label_binarizer.y_type_ :", mlp._label_binarizer.y_type_)

# softmax
print("clf.predict_proba([[2., 2.], [1., 2.]] :",mlp.predict_proba([[2., 2.], [1., 2.]] ))

print("n_outputs_ : ", mlp.n_outputs_)

