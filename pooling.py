import tensorflow as tf

x = tf.layers.Input(shape=[20, 20, 3])
print(x)
y = tf.layers.conv2d(x, filters=6, kernel_size=3, padding='same')
print(y)
p = tf.layers.max_pooling2d(y, pool_size=2, strides=2)
print(p)