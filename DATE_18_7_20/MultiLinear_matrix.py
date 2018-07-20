import  tensorflow as tf

xStudyDataAndCheckDate=[[1.,0.,3.,0.,5.],[0.,2.,0.,4.,0.]]
yTestResult=[1.,2.,3.,4.,5.]

weight=tf.Variable(tf.random_uniform([1,2],-1,1))
bias=tf.Variable(tf.random_uniform([1],-1,1))
#weight = (1x2)행렬 xStudyDataAndCheckDate = (2x5)행렬 ==?(1X5)행렬
#hypothesis = w[0] * x[0] +w[1] *x[1] +b
hypothesis = tf.matmul(weight,xStudyDataAndCheckDate)+bias
cost=tf.reduce_mean((hypothesis-yTestResult)**2)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(loss=cost)

session =tf.Session()
session.run(tf.global_variables_initializer())
for rangeNum in range(1000):
    session.run(train)
    print(rangeNum,session.run(cost))
ww, bb = session.run(weight),session.run(bias)
x_test = [0,4]
print('ww:',ww,'bb',bb)
print("redict :",ww[0][0]*x_test[0]+ww[0][1]*x_test[1]+bb[0])
session.close()
