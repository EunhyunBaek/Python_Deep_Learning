import tensorflow as tf
#구구단
STARTNUMBER=1
ENDNUMBER=10
COUNTPLUS=1
class Hyun_A_group_of_games:
    n=tf.placeholder(tf.float32)
    number=9
    sess=tf.Session()
    def INIT(self):
        Hyun_A_group_of_games.sess.run(tf.global_variables_initializer())
    def CLOSE(self):
        Hyun_A_group_of_games.sess.close()
    def GET_Session(self):
        return Hyun_A_group_of_games.sess
    def Set_Number(num):
        Hyun_A_group_of_games.number=num
    def Get_Number(self):
        return Hyun_A_group_of_games.number
    def Get_Tensor_Num(self):
        return Hyun_A_group_of_games.n
    def Print(self):
        n=Hyun_A_group_of_games.Get_Tensor_Num(0)
        num=Hyun_A_group_of_games.Get_Number(0)
        sess=Hyun_A_group_of_games.GET_Session(0)
        for NUMCOUNT in range(STARTNUMBER,ENDNUMBER,COUNTPLUS):
            print(sess.run((n)*(NUMCOUNT),feed_dict={n:num}))
    def Print2(self):
        left = tf.placeholder(tf.float32)
        right = tf.placeholder(tf.float32)
        multiply = tf.multiply(left, right)
        sess=Hyun_A_group_of_games.GET_Session(0)
        num = Hyun_A_group_of_games.Get_Number(0)
        for NUMCOUNT in range(STARTNUMBER, ENDNUMBER, COUNTPLUS):
            result = sess.run(multiply, feed_dict={left:num, right: NUMCOUNT})
            print('{} X {} = {:2}'.format(num, NUMCOUNT, result))
    def Print3(self):
        dan = Hyun_A_group_of_games.Get_Number(0)
        right = tf.placeholder(tf.int32)
        multiply = tf.multiply(dan, right)
        sess=Hyun_A_group_of_games.GET_Session(0)
        sess.run(tf.global_variables_initializer())
        for i in range(1, 10):
            result = sess.run(multiply, feed_dict={right: i})
            print('{0} X {1} = {2}'.format(dan, i, result))

hyun = Hyun_A_group_of_games
hyun.INIT(0)
hyun.Set_Number(15)
hyun.Print(0)
hyun.Print2(0)
hyun.Print3(0)
hyun.CLOSE(0)