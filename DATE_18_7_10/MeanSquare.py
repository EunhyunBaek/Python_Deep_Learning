#타겟(목표)
t=[0,0,0,0,0,0,0,1,0,0]
#예측 y
y1=[0.1,0,0,0.1,0.05,0.05,0,0.7,0,0]
y2=[0,0.1,0.7,0.05,0.05,0.1,0,0,0,0]

import numpy as np
def Mean_Seq_Err(t,y):
    #return 0.5 *np.sum((t-y)**2)
    return np.sum((t-y)**2)

print(Mean_Seq_Err(np.array(t),np.array(y1)))
print(Mean_Seq_Err(np.array(t),np.array(y2)))