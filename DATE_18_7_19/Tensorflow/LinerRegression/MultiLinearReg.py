import tensorflow as tf
x1=[1.,0.,3.,0.,5.]#공부한 시간
x2=[0.,2.,0.,4.,0.]#출석한 일수
y=[1.,2.,3.,4.,5.]#시험 점수

w1=tf.Variable(tf.random_uniform([1],-1,1))
w2=tf.Variable(tf.random_uniform([1],-1,1))
b=tf.Variable(tf.random_uniform([1],-1,1))

#hypothesis 작성
#1*1 1*5 -> 1*5
hypothesis = w1*x1+w2*x2+b
#cost
cost=tf.reduce_mean((hypothesis-y)**2)
#optimizer
optimizer = tf.train.GradientDescentOptimizer(0.1)
#train
train = optimizer.minimize(loss = cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print("init ",sess.run(w1),sess.run(w2),sess.run(b))
for i in range(1000):
    sess.run(train)
    print(i,sess.run(cost))
print("Hypothesis[",sess.run(hypothesis),"]")
print("w1:",sess.run(w1),"w2:",sess.run(w2),"b:",sess.run(b),"cost:",sess.run(cost))
x_test=[0,4]
w1,w2,bb=sess.run(w1),sess.run(w2),sess.run(b)
print("predict:",w1*x_test[0]+w2*x_test[1]+bb)