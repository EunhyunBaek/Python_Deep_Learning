# coding=utf-8
#LabelBinarizer 모듈 선언
from sklearn.preprocessing import LabelBinarizer

class Hyun_Label_Binarizer:
    ib=LabelBinarizer()
    X=['A','B','C','D','A','B']
    ib.fit(X)
    def Print(self):
        #어떻게 분류 했나
        print(Hyun_Label_Binarizer.ib.classes_)
        #0과 1로 변형된 값
        print(Hyun_Label_Binarizer.ib.transform(Hyun_Label_Binarizer.X))
hyun=Hyun_Label_Binarizer
hyun.Print(0)

