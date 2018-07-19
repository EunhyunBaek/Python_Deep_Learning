# coding=utf-8
import tensorflow as tf

aa=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
add=tf.add(aa,b)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(add,feed_dict={aa:4,b:5}))
sess.close()