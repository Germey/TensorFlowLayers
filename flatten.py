import tensorflow as tf

x = tf.layers.Input(shape=[5, 6])
print(x)
y = tf.layers.flatten(x)
print(y)

x = tf.placeholder(shape=[5, 6, 2], dtype=tf.float32)
print(x)
y = tf.layers.flatten(x)
print(y)
