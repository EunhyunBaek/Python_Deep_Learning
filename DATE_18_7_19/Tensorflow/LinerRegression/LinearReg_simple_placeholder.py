import tensorflow as tf

xx=[1,2,3]
yy=[1,2,3]

w=tf.Variable(tf.random_uniform([1],-1,1))
b=tf.Variable(tf.random_uniform([1],-1,1))

x=tf.placeholder(tf.float32)
x_test=[5,7]

hypothesis = w * x + b
#평균 제곱 오차를 구한다.
cost = tf.reduce_mean((hypothesis-yy)**2)
#옵티마이저를 지정한다(학습 방법을 지정한다)
#optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
#학습 진행
train=optimizer.minimize(loss=cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
#EP
for i in range(10):
    sess.run(train,feed_dict={x:xx})
    print(i,sess.run(cost,feed_dict={x:xx}))
for i in range(len(x_test)):
    print("x=",x_test[i],"predict:",sess.run(hypothesis,feed_dict={x:x_test}))
sess.close()