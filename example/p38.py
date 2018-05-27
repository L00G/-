import tensorflow as tf

a = tf.Variable(0)
add = tf.assign_add(a,1)
saver = tf.train.Saver(max_to_keep=5)
sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(10001):
    sess.run(add)

    if step%1000==0:
        saver.save(sess,'./save/savedata',global_step=step)

