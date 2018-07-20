import tensorflow as tf

def nine_1(dan):
    left = tf.placeholder(tf.float32)
    right = tf.placeholder(tf.float32)
    multiply=tf.multiply(left,right)
    sess=tf.Session()
    sess.run(tf.global_variables_initializer())
    for i in range(1,10):
        result=sess.run(multiply,feed_dict={left:dan,right:i})
        print('{} X {} = {:2}'.format(dan,i,result))
    sess.close()
#nine_1(9)
def nine_2(dan):
    right = tf.placeholder(tf.int32)
    multiply = tf.multiply(dan, right)
    sess=tf.Session()
    sess.run(tf.global_variables_initializer())
    for i in range(1,10):
        result = sess.run(multiply,feed_dict={right:i})
        print('{0} X {1} = {2}'.format(dan,i,result))
    sess.close()
nine_2(9)