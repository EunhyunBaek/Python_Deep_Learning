import tensorflow as tf

value = tf.Variable(0)#변수
one = tf.constant(1)#상수 변하지않음

state = tf.add(value,one)
update = tf.assign(value,state)
