import tensorflow as tf

a = tf.constant(5, dtype=tf.int64)
b = tf.constant(4.21315, dtype="float")
c = tf.constant("english")
d = tf.constant([[3,2,1],[1,2,3]], name = "int_array")

sess = tf.Session()
print(sess.run([a,b,c]))
print(sess.run(d))
sess.close()

