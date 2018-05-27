import tensorflow as tf

a = tf.Variable(0)
add = tf.assign_add(a,1)
saver = tf.train.Saver()
sess = tf.Session()

ckpt = tf.train.get_checkpoint_state('./save')
saver.restore(sess,ckpt.all_model_checkpoint_paths[0])
print(sess.run(a))
saver.restore(sess,ckpt.all_model_checkpoint_paths[1])
print(sess.run(a))
saver.restore(sess,ckpt.all_model_checkpoint_paths[2])
print(sess.run(a))
saver.restore(sess,ckpt.model_checkpoint_path)
print(sess.run(a))

