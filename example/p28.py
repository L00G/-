import tensorflow as tf

x = tf.Variable(5)
x = tf.assign_add(x,1)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(x))
print(sess.run(x))
sess.close()


