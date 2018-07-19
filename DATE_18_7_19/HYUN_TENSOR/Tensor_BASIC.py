import tensorflow as tf

class Hyun_Tensor:
    #세션을 실행할때 순서에 따라 변수가 어떻게 변하는지 확인
    value=tf.Variable(0)
    one=tf.constant(1)
    sess = tf.Session()
    def Add(self):
        return tf.add(Hyun_Tensor.value,Hyun_Tensor.one)
    def State(self):
        return tf.add(Hyun_Tensor.value, Hyun_Tensor.one)
    def Update(self):
        #state 값을 value에 할당하고 할당된 값을 리턴하기 위한 함수
        #state=Hyun_Tensor.State(0)
        return tf.assign(Hyun_Tensor.value,Hyun_Tensor.State(0))
    def INIT(self):
        Hyun_Tensor.sess.run(tf.global_variables_initializer())
    def CLOSE(self):
        Hyun_Tensor.sess.close()
    def Print(self):
        update=Hyun_Tensor.Update(0)
        state=Hyun_Tensor.State(0)
        for _ in range(3):
            print("Update:  ",Hyun_Tensor.sess.run(update),
                  "State:   ",Hyun_Tensor.sess.run(state))
    def Print2(self):
        update = Hyun_Tensor.Update(0)
        state = Hyun_Tensor.State(0)
        for _ in range(3):
           print("State:  ", Hyun_Tensor.sess.run(state),
                 "Update:   ", Hyun_Tensor.sess.run(update))
hyun=Hyun_Tensor
hyun.INIT(0)
hyun.Print(0)
hyun.Print2(0)
hyun.CLOSE(0)