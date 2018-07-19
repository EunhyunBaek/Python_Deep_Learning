import tensorflow as tf
import numpy as np

cars=np.loadtxt('cars.csv',delimiter=',',unpack=True)
x=cars[0]
y=cars[1]

w=tf.Variable(tf.random_uniform([1],-1,1))
b=tf.Variable(tf.random_uniform([1],-1,1))

hypothesis= w * x + b
cost=tf.reduce_mean((hypothesis-y)**2)
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.0001)
train=optimizer.minimize(loss = cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(1000):
    sess.run(train)

ww,bb=sess.run(w),sess.run(b)
print('w:',ww,'b:',bb,'cost:',sess.run(cost))
sess.close()