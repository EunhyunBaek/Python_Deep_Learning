import pandas as pa
import matplotlib.pylab as plt
def getDifferential(f,x):#미분식
    #It means 1 × 10-5. In other words, 0.00001.
    h=1e-4  #x의 증분값 10^-4
    #print(h)
    return (f(x+h)- f(x-h))/(2*h)    #미분 방정식
def equation1(x):
    #**  제곱수 표시
    return 10*x**3 + 5*x**2 + 4*x   #10*x^3+5x^2+4x
def equation2(x):
    return 0.01 *x**2 +0.1*x #0.01*x^2 + 0.1*x
d= getDifferential(equation1,5)
#print(d)


