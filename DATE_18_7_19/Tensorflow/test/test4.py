import tensorflow as tf
#placeholder를 사용한 구구단 세팅
n=tf.placeholder(tf.float32)
sess= tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(1,9,1):
    print(sess.run((n)*(i),feed_dict={n:9}))
sess.close()