import tensorflow as tf

x = tf.constant(5)
y = tf.constant(4)

addxy = tf.add(x, y) # x + y
subxy = tf.subtract(x, y) # x - y
mulxy = tf.multiply(x, y) # x * y
divxy = tf.truediv(x, y) # x / y
modxy = tf.mod(x, y) # x % y

sess = tf.Session()
print(sess.run([addxy, subxy, mulxy, divxy, modxy]))
sess.close()