import tensorflow as tf

x_data = [1, 2, 3, 4, 5]; y_data = [1, 2, 3, 4, 5]

W = tf.Variable(-0.51)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

cal = W * X
cost = tf.losses.absolute_difference(cal, Y)
#cost = tf.abs(tf.reduce_sum(Y - cal =))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(500):
    _, cost_val = sess.run([train, cost], feed_dict={X: x_data, Y: y_data})
    print(step,"csot:",cost_val,"W: ",sess.run(W))

print("X: 10, Y:", sess.run(cal, feed_dict={X: 10}))
print("X: 200, Y:", sess.run(cal, feed_dict={X: 200}))

sess.close()