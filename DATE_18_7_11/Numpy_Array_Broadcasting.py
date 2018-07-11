import numpy as np
class HYUN_Numpy_BroadCasting:
    def Numpy_BroadCasting_Procession_TO_Intiger(self):
        x = np.array([[2, 3], [4, 5]])
        y = 5
        x1 = x + y
        print('x type:', type(x))
        print('y type:', type(y))
        print(x + y)
    def Numpy_BroadCasting_Procession_SUM_Procession(self):
        x=np.array([[2,3],[7,8]])
        y=np.array([5,10])#[5,10],[5,10]으로 변환되어서 계산됨 주의
        x2=x+y
        print("x shape:", x.shape)
        print("y shape:", y.shape)
        print("x2 shape:", x2.shape)
        print('x2 : ',x2)

Hyun=HYUN_Numpy_BroadCasting
Hyun.HYUN_Numpy_BroadCasting_Procession_TO_Intiger(0)
Hyun.HYUN_Numpy_BroadCasting_Procession_SUM_Procession(0)