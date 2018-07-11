import numpy as np
'''
x = np.array([1.0,2.0,3.0,4.0])
print(x)
print(type(x))
print(x.shape)
'''
class Hyun_Numpy:
    def Numpy_Array(self):
        x1 = np.array([[1, 2, 3], [4, 5, 6]])
        print(x1)
        print(type(x1))
        print(x1.shape)

    def Numpy_Array_Zero(self):
        x = np.zeros(10)
        print(x)
        x1 = np.zeros((3, 2))
        print(x1)

    def Numpy_Array_Ones(self):
        x = np.ones(10)
        print(x)
        x1 = np.ones((3, 2))
        print(x1)

Hyun=Hyun_Numpy
Hyun.Numpy_Array(0)
Hyun.Numpy_Array_Zero(0)
Hyun.Numpy_Array_Ones(0)