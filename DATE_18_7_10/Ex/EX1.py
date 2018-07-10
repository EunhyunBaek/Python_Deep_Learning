
#ex
#식 f= x**2+y**2
#점 x3,y=4에서의 편미분을 구하시오

def getDifferential(f,x):#미분식
    #It means 1 × 10-5. In other words, 0.00001.
    h=1e-4  #x의 증분값 10^-4
    #print(h)
    return (f(x+h)- f(x-h))/(2*h)    #미분 방정식

def Math_Differentiation_X_Function(x):
    return x*x + 4.0 ** 2.0
def Math_Differentiation_Y_Function(y):
    return 3.0 ** 2.0 + y*y
def Math_Differentiation_X_Function2(x):
    return x**2 + 4.0 ** 2.0
def Math_Differentiation_Y_Function2(y):
    return 3.0 ** 2.0 + y**2
print(getDifferential(Math_Differentiation_X_Function,3.0))
print(getDifferential(Math_Differentiation_Y_Function,4.0))