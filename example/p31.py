import tensorflow as tf

x = tf.constant(5)
y = tf.constant(4)

a = tf.constant(True)
b = tf.constant(False)

aaxy = tf.bitwise.bitwise_and(x, y)
aoxy = tf.bitwise.bitwise_or(x, y)
axxy = tf.bitwise.bitwise_xor(x, y)

laab = tf.logical_and(a, b)  # a & b
loab = tf.logical_or(a, b)  # a | b
lxab = tf.logical_xor(a, b)  # a ^ b
na = tf.logical_not(a)  # ~a

sess = tf.Session()
print(sess.run([aaxy, aoxy, axxy]))
print(sess.run([laab, loab, lxab, na]))
sess.close()