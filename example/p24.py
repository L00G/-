import tensorflow as tf

a = tf.Variable(5)
b = tf.Variable(4.1151, name="float", dtype=tf.float16)
c = tf.Variable("english", dtype=tf.string)
d = tf.Variable(tf.ones([4, 4]))

init = tf.global_variables_initializer()
init_d = tf.variables_initializer([d])

sess = tf.Session()
sess.run(init)
sess.run(init_d)

print(a, b, c, d, sep="\n")
print(sess.run([a, b, c]))
print(sess.run(d))
sess.close()