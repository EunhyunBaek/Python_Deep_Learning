import tensorflow as tf
import numpy as np
#InputTrainData is 6X1
inputtrainData = \
            [
            [1.,1.,2.],
            [1.,2.,3.],
            [1.,2.,4.],
            [1.,5.,3.],
            [1.,7.,5.],
            [1.,8.,4.]
            ]
#OutputTrainData is 6X1
outputtrainData=\
            [
            [0],
            [0],
            [0],
            [1],
            [1],
            [1]
            ]
weight = tf.Variable(tf.random_uniform([3,1],-1,1))
#브로드 케스팅 기능을 사용하기 위해 numpy 사용
testoutputData=np.array(outputtrainData)
#resultData = 6X3,3X1 -->6X1
resultData=tf.matmul(inputtrainData,weight)
#this hypothesis is sigmoied
hypothesis = 1/(1+tf.exp(-resultData))
cost =tf.reduce_mean(testoutputData*-tf.log(hypothesis)+(1-testoutputData)*-tf.log(1-hypothesis))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train=optimizer.minimize(loss=cost)
sess=tf.Session()
sess.run(tf.global_variables_initializer())

for rangeNum in range(10):
    sess.run(train)
    print(rangeNum,sess.run(cost))
sess.close()