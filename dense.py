import tensorflow as tf

x = tf.layers.Input(shape=[32])
print(x)
y1 = tf.layers.dense(x, 16, activation=tf.nn.relu)
print(y1)
y2 = tf.layers.dense(y1, 5, activation=tf.nn.sigmoid)
print(y2)