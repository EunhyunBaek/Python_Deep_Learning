from sklearn.preprocessing import StandardScaler, MinMaxScaler, minmax_scale
import numpy as np
import pandas as pd
stdscaler = StandardScaler()
minmax_scaler = MinMaxScaler()
"""
함수의 파라미터에 -1이 들어가면 특별한 의미를 갖는데, 다른 나머지 차원 크기를 맞추고 남은 크기를 해당 차원에 할당해 준다는 의미입니다
>> arr = np.zeros(64,64,3) # 64 * 64 size image with RGB channels 
>> arr = getImage() # Image loaded 
>> arr.shape >> [64,64,3] 
>> b = arr.reshape(64*64,3) 
>> b.shape 
>> [4096,3] 
>> c = arr.reshape(16,16,-1) # -1은 1차와 2차의 크기를 16과 16으로 맞추고 남은 나머지라는 뜻입니다. 
>> c.shape 
>> [16,16,48] # (64*64*3) / (16 * 16) = 48이므로 배열의 세 번째 차원의 크기는 48이 됩니다.
"""
#평균 표준편차 스케일링
input_data = (np.arange(5, dtype=np.float) - 2).reshape(-1, 1)
print((np.arange(5, dtype=np.float) - 2).reshape(-1, 1) )
print((np.arange(5, dtype=np.float) - 2) )
minmax_scale_data = minmax_scaler.fit_transform(input_data)
print("평균 : " , minmax_scale_data.mean(axis=0))
print("표준편차 : ",minmax_scale_data.std(axis=0))
df1 = pd.DataFrame(np.hstack([input_data,
minmax_scale(input_data)]),

columns=["input_data", "minmax_scale(input_data)"])

print(df1)