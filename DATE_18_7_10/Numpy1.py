import numpy as np
import numpy.linalg as lin
class Numpy:
    a = np.array([[1, 2, 3], [3, 4, 5]])
    b = np.array([[7, 8], [9, 10], [11, 12]])
    def Shape(self):
        print(Numpy.a.shape)
        print(Numpy.a)
        print(Numpy.b.shape)
        print(Numpy.b)

    def Dot(self):
        print(np.dot(Numpy.a,Numpy.b))

class NumpyLinalg:
    a= np.array([[1,2],[4,5]])
    def Shape(self):
        print(Numpy.a.shape)
        print(Numpy.a)
    def Lin_Inv(self):#역행열 inverse
        c=lin.inv(NumpyLinalg.a)
        print(c)
        NumpyLinalg.Dot(NumpyLinalg.a,c)
    def Dot(a,b):
        e=np.dot(a,b)
        print(e)


print("a")
Numpy.Shape(0)
print("b")
Numpy.Shape(0)
print("a*b")
Numpy.Dot(0)

NumpyLinalg.Shape(0)
NumpyLinalg.Lin_Inv(0)
