import tensorflow as tf

x = tf.layers.Input(shape=[32])
print(x)
y = tf.layers.dense(x, 16, activation=tf.nn.softmax)
print(y)

data = tf.constant([1, 2, 3])
x = tf.layers.Input(tensor=data)
print(x)
