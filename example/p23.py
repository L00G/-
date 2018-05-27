import tensorflow as tf

a = tf.ones([4, 4])
b = tf.zeros([4, 4])
c = tf.fill([2, 2], 14)
d = tf.constant(-14, shape=[2, 2])

# tf.set_random_seed(1)
e = tf.truncated_normal([4, 4], seed=1)
f = tf.random_normal([4, 4])
g = tf.random_uniform([2, 3], minval=0, maxval=10)

h = tf.range(start=1, limit=7, delta=1)  # 1~6
i = tf.range(10)  # 0~9

sess = tf.Session()

print(sess.run([a, b, c, d, e, f, g, h, i]))
sess.close()