import tensorflow as tf

filename_queue = tf.train.string_input_producer(
    ['learning-data-1.csv', 'learning-data-2.csv'])
key, value = tf.TextLineReader().read(filename_queue)

x, y, z = tf.decode_csv(value, [[0], [''], [0.]], ',')

sess = tf.Session()
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(
    sess=sess, coord=coord)

for i in range(15):
    print(sess.run([x, y, z]))

coord.request_stop()
coord.join(threads)

