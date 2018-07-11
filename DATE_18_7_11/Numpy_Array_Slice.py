import numpy as np
class HYUN_Slice():
    def List_Slice(self):  # 값을 복사해서 사용하기에 원본 손상 x
        x1 = list(list(range(10)))
        x2 = x1[0:3]
        print("x2                   : ", x2)
        x2[1] = 100
        print("change 100 in x2[1]  : ", x2)
        print("x1                   : ", x1)
    def Numpy_Slice(self):  # Point 개념 원본 손상 o
        y1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        print("y1                   : ", y1)
        y2 = y1[0:3]
        print("y1                   : ", y1)
        y2[1] = 100
        print("change 100 in y2[1]  : ", y2)
        print("y1                   : ", y1)
Hyun=HYUN_Slice
Hyun.List_Slice(0)
Hyun.Numpy_Slice(0)