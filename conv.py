import tensorflow as tf

x = tf.layers.Input(shape=[20, 20, 3])
y = tf.layers.conv2d(x, filters=6, kernel_size=2, padding='same')
print(y)

y = tf.layers.conv2d(x, filters=6, kernel_size=2)
print(y)

y = tf.layers.conv2d(x, filters=6, kernel_size=[2, 3])
print(y)

y = tf.layers.conv2d(x, filters=6, kernel_size=[2, 3], strides=[2, 2])
print(y)

y = tf.layers.conv2d(x, filters=6, kernel_size=2, activation=tf.nn.relu, use_bias=False)
print(y)

y = tf.layers.conv2d_transpose(x, filters=6, kernel_size=2, strides=2)
print(y)

y = tf.layers.separable_conv2d(x, filters=6, kernel_size=2, strides=2)
print(y)
