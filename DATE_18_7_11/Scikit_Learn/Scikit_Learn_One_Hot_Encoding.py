from sklearn.preprocessing import OneHotEncoder
import numpy as np

class Hyun_One_Hot_Encoding:
    ohe=OneHotEncoder()
    X=np.array([[2],[1],[0]])
    def Print(self):
        print(Hyun_One_Hot_Encoding.ohe)
        print(Hyun_One_Hot_Encoding.X)
        print(Hyun_One_Hot_Encoding.ohe.fit_transform(Hyun_One_Hot_Encoding.X).toarray())

hyun=Hyun_One_Hot_Encoding
hyun.Print(0)