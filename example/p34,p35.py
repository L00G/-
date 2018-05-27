import tensorflow as tf

filename_queue = tf.train.string_input_producer(
    ['learning-data-1.csv', 'learning-data-2.csv'])
key, value = tf.TextLineReader().read(filename_queue)

xyz = tf.decode_csv(value,  [[0], [''], [0.]], ',')

x_batch, y_batch, z_batch = tf.train.batch(
    [xyz[0:1], xyz[1:2], xyz[2:3]], batch_size=3)

sess = tf.Session()

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(4):
    x_data, y_data, z_data = sess.run([x_batch, y_batch, z_batch])
    
    print('step #',step)
    for i in range(3):
        print(x_data[i],y_data[i],z_data[i])

coord.request_stop()
coord.join(threads)
