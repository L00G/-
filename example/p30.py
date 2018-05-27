import tensorflow as tf

x = tf.constant(5)
y = tf.constant(4)

lxy = tf.less(x, y)  # x<y
lq = tf.less_equal(x, y)  # x<=y
gxy = tf.greater(x, y)  # x>y
gexy = tf.greater_equal(x, y)  # x>=y
exy = tf.equal(x, y)

sess = tf.Session()
print(sess.run([lxy, lq, gxy, gexy, exy]))
sess.close()

