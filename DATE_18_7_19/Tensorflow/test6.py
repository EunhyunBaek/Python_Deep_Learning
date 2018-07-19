import tensorflow as tf

xTrainData = [1, 2, 3, 4, 5, 6, 7, 8, 9]
yTrainData = [1, 2, 3, 4, 5, 6, 7, 8, 9]

weight=tf.Variable(tf.random_uniform([1],-1,1))
bias=tf.Variable(tf.random_uniform([1],-1,1))
xTestData = [5,7]
#hypotheses 설정
#hypotheses = ft.add(tf.multiply(x,w),b)
hypothesis = weight * xTrainData + bias
#평균 제곱 오차를 구한다.
cost = tf.reduce_mean((hypothesis-yTrainData)**2)
#옵티마이저를 지정한다(학습 방법을 지정한다)
#optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
#학습 진행
train=optimizer.minimize(loss=cost)
sess= tf.Session()
sess.run(tf.global_variables_initializer())
#epoch를 10번 수행
for i in range(10):
    sess.run(train)
print("w:",sess.run(weight),"b:",sess.run(bias),"cost:",sess.run(cost))
for i in range(len(xTestData)):
    print("x=",xTestData[i],"predict:",sess.run(weight*xTestData[i]+bias))
sess.close()