import tensorflow as tf

a1 = tf.constant([[1,5],[2,3]])
a2 = tf.constant([[3,4],[4,5]])

b1 = tf.constant(100)

adda = tf.matmul(a1, a2)
subb = tf.mod(adda,b1)

sess = tf.Session()
print(sess.run([adda]))
print(sess.run([subb]))
sess.close()