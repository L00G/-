import tensorflow as tf

x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.int32)

addxy = tf.add(x, y)
subxy = tf.subtract(addxy, z)

sess = tf.Session()
z = sess.run(subxy, feed_dict={x:4,y:3,z:2})
print(z)
sess.close()

