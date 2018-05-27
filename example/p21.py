import tensorflow as tf

sess = tf.InteractiveSession()

a = tf.Variable(5)
tf.global_variables_initializer().run()
a.initializer.run()
add = tf.add(a,a).eval()

sess.close()

with tf.Session():
    tf.add(5,5).eval()
