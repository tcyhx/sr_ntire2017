import tensorflow as tf

def build_model(x):
    prev_x = x
    x = tf.layers.conv2d(x, 64, 3, padding='same', activation=tf.sigmoid, name='conv1')
    x = tf.layers.conv2d(x, 64, 3, padding='same', activation=tf.sigmoid, name='conv2')
    x = tf.layers.conv2d(x, 64, 3, padding='same', activation=tf.sigmoid, name='conv3')
    x = tf.layers.conv2d(x, 1, 1, padding='same', activation=None, name='conv4')
    x += prev_x
    return x