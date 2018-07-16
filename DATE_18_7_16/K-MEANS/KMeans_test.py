# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:31:02 2017

@author: BEAST
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:02:19 2017

@author: BEAST
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.metrics import silhouette_samples, silhouette_score

X_train = np.array([[10, 2],[5, 8],[7, 2], [4, 7],[3, 9],[2, 9],
              [0, 8], [1, 7],[9, 3], [7, 4],[6, 2],[4, 6],
              [1, 9], [2, 7],[10, 3],[8, 4],[9, 1],[5, 3],[11,3],[9,2]
              ])
plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], s=100, label='input data')  # X1 값 , X2 값 선정
#backhyun
#init_point = np.array([[0,0],[10,10]])
init_point = np.array([[0,0],[10,10],[20,20]])
plt.scatter(init_point[0, 0], init_point[0, 1], label='init point 1', c='r', s=100)
plt.scatter(init_point[1, 0], init_point[1, 1], label='init point 2', c='b', s=100)
#backhyun
plt.scatter(init_point[2, 0], init_point[2, 1], label='init point 3', c='g', s=100)
plt.legend()

#plt.show()

#epoche = 100
#plt.figure()
i = 1
while  i <= 10 :
    model = KMeans(n_clusters=3, init=init_point, n_init=1, max_iter=i, random_state=0) # 모델 설정
    model.fit(X_train)  # 학습

    c0, c1,c2 = model.cluster_centers_  # 중심점 찾기
    #backhyun
    #print("c0 ", c0, "C1", c1)
    print("c0 ", c0, "C1", c1,"C2",c2)
    print(model.labels_)
    plt.figure()
#    plt.subplot(1, 4, i)
    plt.scatter(X_train[model.labels_==0,0], X_train[model.labels_==0,1], s=100, marker='v', c='r', label='class 0')
    plt.scatter(X_train[model.labels_==1,0], X_train[model.labels_==1,1], s=100, marker='^', c='b', label='class 1')
    #backhyun
    plt.scatter(X_train[model.labels_==2,0], X_train[model.labels_==2,1], s=100, marker='o', c='g', label='class 2')

    plt.scatter(c0[0], c0[1], s=100, c="r", label='Centriod 0')
    plt.scatter(c1[0], c1[1], s=100, c="b", label='Centriod 1')
    #backhyun
    plt.scatter(c2[0], c2[1], s=100, c="g", label='Centriod 2')
    plt.xlabel("X0")
    plt.ylabel("X1")
    #backhyun
    #plt.title("{4} Loop \n Centriod 0 [{0} , {1}]\n Centriod 1 [{2}, {3}]".format(c0[0],c0[1], c1[0], c1[1], i))
    plt.title("{6} Loop \n Centriod 0 [{0} , {1}]\n Centriod 1 [{2}, {3}]\n Centriod 2 [{4}, {5}]".format(c0[0],c0[1], c1[0], c1[1],c2[0],c2[1], i))
    plt.legend()
#    plt.show()
    i += 1
plt.show()
#backhyun
def kmeans_check_data(c0, c1,c2):
    df = pd.DataFrame(np.hstack([X_train,
                      np.linalg.norm(X_train - c0, axis=1)[:, np.newaxis],
                                np.linalg.norm(X_train - c1, axis=1)[:, np.newaxis],
                                    np.linalg.norm(X_train - c2, axis=1)[:, np.newaxis],
                                model.labels_[:, np.newaxis]]),
                    columns=["x0", "x1", "distance 0", "distance 1", "cluster"])
    return df

result = kmeans_check_data(c0, c1, c2)
print(result)



#print(np.linalg.norm(X - c0, axis=1)[:, None])  # 가로를 세로로 세

print(model.score(X_train))

print("silhouette_score :", silhouette_score(X_train, model.labels_,
                                      metric='euclidean',
                                      sample_size=len(X_train)))
