import tensorflow as tf

a = tf.placeholder(tf.int64)
b = tf.placeholder("float", shape=[None, None])
c = tf.placeholder(tf.string, shape=[2])

sess = tf.Session()
x, y, z = sess.run([a, b, c], feed_dict={a: [1, 2], b: [[2, 1], [5, 2]], c: ["one", "two"]})
print(x, y, z, sep='\n')
sess.close()