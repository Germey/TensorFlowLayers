import tensorflow as tf

x = tf.layers.Input(shape=[32])
x = tf.layers.batch_normalization(x)
y = tf.layers.dense(x, 20)
print(x)