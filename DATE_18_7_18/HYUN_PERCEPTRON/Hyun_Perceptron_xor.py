# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import numpy as np
import seaborn as sns

class HYUN_MLPCLASSIFIER:
    X = np.array([[0, 0], [1, 0], [0, 1], [1, 1],[0, 0], [0, 0], [0, 0], [0, 0]])
    y = np.array([0, 1, 1, 0,0, 1, 1, 0])
    #mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10, 4]).fit(X, y)
    #mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[4]).fit(X, y)
    mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[4,4,4]).fit(X, y)
    def Plot_mlp(ppn):
        print(HYUN_MLPCLASSIFIER.Plot_mlp)
        # plt.figure(figsize=(12, 8), dpi=60)
        #    model = Perceptron(n_iter=10, eta0=0.1, random_state=1).fit(X, y)
        model = ppn
        XX_min = HYUN_MLPCLASSIFIER.X[:, 0].min() - 1;
        XX_max = HYUN_MLPCLASSIFIER.X[:, 0].max() + 1;
        YY_min = HYUN_MLPCLASSIFIER.X[:, 1].min() - 1;
        YY_max = HYUN_MLPCLASSIFIER.X[:, 1].max() + 1;
        XX, YY = np.meshgrid(np.linspace(XX_min, XX_max, 1000), np.linspace(YY_min, YY_max, 1000))
        ZZ = model.predict(np.c_[XX.ravel(), YY.ravel()]).reshape(XX.shape)
        cmap = matplotlib.colors.ListedColormap(sns.color_palette("Set3"))
        plt.contourf(XX, YY, ZZ, cmap=cmap)
        plt.scatter(x=HYUN_MLPCLASSIFIER.X[HYUN_MLPCLASSIFIER.y == 0, 0], y=HYUN_MLPCLASSIFIER.X[HYUN_MLPCLASSIFIER.y == 0, 1], s=200, linewidth=2, edgecolor='k', c='y', marker='^', label='0')
        plt.scatter(x=HYUN_MLPCLASSIFIER.X[HYUN_MLPCLASSIFIER.y == 1, 0], y=HYUN_MLPCLASSIFIER.X[HYUN_MLPCLASSIFIER.y == 1, 1], s=200, linewidth=2, edgecolor='k', c='r', marker='s', label='1')
        plt.xlim(XX_min, XX_max)
        plt.ylim(YY_min, YY_max)
        plt.grid(False)
        plt.xlabel("X1")
        plt.ylabel("X0")
        plt.legend()
        plt.show()
    def Print(self):
        print(HYUN_MLPCLASSIFIER.Print)
        print("학습 결과: ",HYUN_MLPCLASSIFIER.mlp.predict(HYUN_MLPCLASSIFIER.X))
        print("신경망 깊이: ",HYUN_MLPCLASSIFIER.mlp.n_layers_)
        print("len(mlp.coefs_): ",len(HYUN_MLPCLASSIFIER.mlp.coefs_))
        print("mlp.n_outputs_ : ", HYUN_MLPCLASSIFIER.mlp.n_outputs_)
        print("mlp.classes_:", HYUN_MLPCLASSIFIER.mlp.classes_)

        print(HYUN_MLPCLASSIFIER.Print)
        for i in range(len(HYUN_MLPCLASSIFIER.mlp.coefs_)):
            number_neurons_in_layer = HYUN_MLPCLASSIFIER.mlp.coefs_[i].shape[1]
            print("number_neurons_in_layer :", number_neurons_in_layer, ' i : ', i)
            for j in range(number_neurons_in_layer):
                weights = HYUN_MLPCLASSIFIER.mlp.coefs_[i][:, j]
                print(i, j, weights, end=", ")
                print()
            print()
hyun = HYUN_MLPCLASSIFIER
hyun.Plot_mlp(hyun.mlp)
hyun.Print(0)
