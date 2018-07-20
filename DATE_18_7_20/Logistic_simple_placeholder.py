import tensorflow as tf
import numpy as np

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
x=tf.placeholder(tf.float32)
weight = tf.Variable(tf.random_uniform([3,1],-1,1))
testoutputData=np.array(outputtrainData)
resultData=tf.matmul(inputtrainData,weight)
hypothesis = 1/(1+tf.exp(-resultData))
cost =tf.reduce_mean(testoutputData*-tf.log(hypothesis)+(1-testoutputData)*-tf.log(1-hypothesis))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train=optimizer.minimize(loss=cost)
sess=tf.Session()
sess.run(tf.global_variables_initializer())
for rangeNum in range(100):
    sess.run(train,feed_dict={x:inputtrainData})
    print(rangeNum,sess.run(cost,feed_dict={x:inputtrainData}))
y_hat=sess.run(hypothesis,feed_dict={x:[[1.,7.,2.],[1.,3.,7]]})
print("y_hat",y_hat)
sess.close()