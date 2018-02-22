import tensorflow as tf

x = tf.layers.Input(shape=[32])
print(x)
y = tf.layers.dense(x, 16, activation=tf.nn.softmax)
print(y)
d = tf.layers.dropout(y, rate=0.2)
print(d)
