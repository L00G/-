import tensorflow as tf

a1 = tf.constant(1)
a2 = tf.constant(3.5)

add = tf.add(tf.cast(a1,tf.float32), a2)

sess = tf.Session()
print(sess.run(add))
sess.close()