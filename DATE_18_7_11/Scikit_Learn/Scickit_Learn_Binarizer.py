# coding=utf-8
import numpy as np
from sklearn.preprocessing import Binarizer

class Hyun_Binarizer:
    #default threshold=0.0
    binarizer = Binarizer()
    binarizer1 = Binarizer(threshold=1.5)

    X = np.array([[1, -1], [-1, 0], [0, 2]])

    def Print(self):
        print(Hyun_Binarizer.Print)
        print("X :\n", Hyun_Binarizer.X)
        #similer cv threshold
        print("변환 값 :\n", Hyun_Binarizer.binarizer.transform(Hyun_Binarizer.X))
        print("임계 값 :\n",Hyun_Binarizer.binarizer1.transform(Hyun_Binarizer.X))
hyun=Hyun_Binarizer
hyun.Print(0)
