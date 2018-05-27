import tensorflow as tf

x = tf.constant(5,dtype=tf.int32, name="int_x")
y = tf.placeholder(shape = [2,2],dtype = tf.int32, name="placehoder_y")
addxy = tf.add(x, y, name = 'add_X_Y')
lxy = tf.less(x, addxy, name = 'x_less_then_addxy')

sess = tf.Session()
print(x,y,addxy,lxy,sep='\n')

sess.close()