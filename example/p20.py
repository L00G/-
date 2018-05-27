import tensorflow as tf

sess = tf.Session()
sess.run(tf.add(5,5))
sess.close()

with tf.Session() as sess:
    sess.run(tf.add(5,5))
