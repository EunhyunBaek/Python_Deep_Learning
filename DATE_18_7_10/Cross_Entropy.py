#타겟(목표)
t=[0,0,0,0,0,0,0,1,0,0]
#예측 y
y1=[0.1,0,0,0.1,0.05,0.05,0,0.7,0,0]
y2=[0,0.1,0.7,0.05,0.05,0.1,0,0,0,0]

import numpy as np

def Cross_Entropy(t,y):
    tmp= 1e-7
    return -np.sum(t*np.log(y+tmp))

print(Cross_Entropy(np.array(t),np.array(y1)))
print(Cross_Entropy(np.array(t),np.array(y2)))

