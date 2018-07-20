import  tensorflow as tf

class Hyun_MultiLinear_Matrix:
    xStudyDataAndCheckDateData = [[1., 0., 3., 0., 5.], [0., 2., 0., 4., 0.]]
    yTestResultData = [1., 2., 3., 4., 5.]
    # bias 대신에 w0 추가 (w0 = bias 와 같이 절편 형시으로 표기됨)
    xStudyDataAndCheckDateData.insert(0, [1., 1., 1., 1., 1.])
    weight = tf.Variable(tf.random_uniform([1, 3], -1, 1))

    def Get_Hypothesis(self):
        return tf.matmul(Hyun_MultiLinear_Matrix.weight,Hyun_MultiLinear_Matrix.xStudyDataAndCheckDateData)
    def Get_Cost(self):
        hypothesis = Hyun_MultiLinear_Matrix.Get_Hypothesis(0)
        return tf.reduce_mean((hypothesis-Hyun_MultiLinear_Matrix.yTestResultData)**2)
    def Get_Optimizer(self):
        return tf.train.GradientDescentOptimizer(learning_rate=0.1)
    def Get_Train(self):
        optimizer = Hyun_MultiLinear_Matrix.Get_Optimizer(0)
        return optimizer.minimize(loss=Hyun_MultiLinear_Matrix.Get_Cost(0))

session =tf.Session()
session.run(tf.global_variables_initializer())

for rangeNum in range(1000):
    session.run(Hyun_MultiLinear_Matrix.Get_Train(0))
    print(rangeNum,session.run(Hyun_MultiLinear_Matrix.Get_Cost(0)))
ww = session.run(Hyun_MultiLinear_Matrix.weight)
x_test = [0,4]
print('ww:',ww)
#ww[0][0] <- 바이어스
print("redict :",ww[0][0]*x_test[0]+ww[0][1]*x_test[1]+ww[0][0])
session.close()
