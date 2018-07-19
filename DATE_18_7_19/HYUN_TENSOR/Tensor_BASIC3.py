import tensorflow as tf

class Hyun_Train_GradientDescentOptimizer:
    xtraindata = [1,2,3]
    ytraindata = [1,2,3]
    xtestdata = tf.placeholder(tf.float32)
    x_test = [5, 7]
    def Init_Session(self):
        return tf.Session()
    def Close_Session(sess):
        sess.close()
    def Get_Weight(self):
        print("Get_Weight:",tf.Variable(tf.random_uniform([1], -1, 1)))
        return tf.Variable(tf.random_uniform([1], -1, 1))
    def Get_Bias(self):
        print("Get_Bias:",tf.Variable(tf.random_uniform([1], -1, 1)))
        return tf.Variable(tf.random_uniform([1], -1, 1))
    def Get_Hypothesis(self):
        weight = Hyun_Train_GradientDescentOptimizer.Get_Weight(0)
        xtraindata = Hyun_Train_GradientDescentOptimizer.xtraindata
        bias = Hyun_Train_GradientDescentOptimizer.Get_Bias(0)
        print("Get_Hypothesis:weight",weight)
        print("Get_Hypothesis:xtraindata",xtraindata)
        print("Get_Hypothesis:",bias)
        return weight * xtraindata + bias
    def Get_Cost(self):
        ytraindata = Hyun_Train_GradientDescentOptimizer.ytraindata
        hypothesis= Hyun_Train_GradientDescentOptimizer.Get_Hypothesis(0)
        print("Get_Cost:ytraindata",ytraindata)
        print("Get_Cost:hypothesis",hypothesis)
        return tf.reduce_mean((hypothesis - ytraindata) ** 2)
    def Get_Train(self):
        cost = Hyun_Train_GradientDescentOptimizer.Get_Cost(0)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
        print("Get_Train:",cost)
        print("Get_Train:",optimizer)
        return optimizer.minimize(loss=cost)
    def Show(RANGECOUNT,sess):
        train = Hyun_Train_GradientDescentOptimizer.Get_Train(0)
        xtraindata=Hyun_Train_GradientDescentOptimizer.xtraindata
        x_test=Hyun_Train_GradientDescentOptimizer.xtestdata
        x = tf.placeholder(tf.float32)
        hypothesis= Hyun_Train_GradientDescentOptimizer.Get_Hypothesis(0)
        print("Show:train",train)
        print("Show:xtraindata", xtraindata)
        print("Show:x_test", x_test)
        print("Show:x", x)

        for COUNTNUMBER in range(RANGECOUNT):
            print("forL:",COUNTNUMBER)
            sess.run(train)
        #for COUNTNUMBER in range(RANGECOUNT):
        #    sess.run(train,feed_dict={x:xtraindata})
        #for i in range(len(x_test)):
        #    print("x=", x_test[i], "predict:", sess.run(hypothesis, feed_dict={x: x_test}))

hyun =Hyun_Train_GradientDescentOptimizer
#sess=Hyun_Train_GradientDescentOptimizer.Init_Session(0)
sess=tf.Session()
sess.run(tf.global_variables_initializer())
###
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

###
#hyun.Show(100,sess)
Hyun_Train_GradientDescentOptimizer.Close_Session(sess)