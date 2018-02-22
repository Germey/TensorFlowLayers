import tensorflow as tf

x = tf.layers.Input(shape=[32])
dense = tf.layers.Dense(16, activation=tf.nn.relu)
y = dense.apply(x)
print(y)
