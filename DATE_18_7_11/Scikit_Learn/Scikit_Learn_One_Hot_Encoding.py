from sklearn.preprocessing import OneHotEncoder
import numpy as np

class Hyun_One_Hot_Encoding:
    ohe=OneHotEncoder()
    X=np.array([[2],[1],[0]])
    def Print(self):
        print(Hyun_One_Hot_Encoding.ohe)
        print(Hyun_One_Hot_Encoding.X)
        print(Hyun_One_Hot_Encoding.ohe.fit_transform(Hyun_One_Hot_Encoding.X).toarray())
        #입력 값이 몇 개의 분류로 구분되는지 확인
        print(Hyun_One_Hot_Encoding.ohe.n_values_)
        #one hot encoding 시 벡터의 원소 값들이 어떻게 나뉘는지 표현
        print(Hyun_One_Hot_Encoding.ohe.feature_indices_)
        #one hot encoding에 사용되는 색인 값
        print(Hyun_One_Hot_Encoding.ohe.active_features_)
hyun=Hyun_One_Hot_Encoding
hyun.Print(0)