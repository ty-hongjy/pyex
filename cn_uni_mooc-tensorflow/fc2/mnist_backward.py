import os
import configparser

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import mnist_forward

# 加载现有配置文件
conf = configparser.ConfigParser()
# 读取配置文件
conf.read('parameter.ini')
BATCH_SIZE = conf.getint('backward', 'BATCH_SIZE')
LEARNING_RATE_BASE = conf.getfloat('backward', 'LEARNING_RATE_BASE')
LEARNING_RATE_DECAY = conf.getfloat('backward', 'LEARNING_RATE_DECAY')
REGULARIZER = conf.getfloat('backward', 'REGULARIZER')
STEPS = conf.getint('backward', 'STEPS')
MOVING_AVERAGE_DECAY = conf.getfloat('backward', 'MOVING_AVERAGE_DECAY')
MODEL_SAVE_PATH = conf.get('backward', 'MODEL_SAVE_PATH')
MODEL_NAME = conf.get('backward', 'MODEL_NAME')

print('BATCH_SIZE:', BATCH_SIZE)
print('LEARNING_RATE_BASE:', LEARNING_RATE_BASE)
print('LEARNING_RATE_DECAY:', LEARNING_RATE_DECAY)
print('REGULARIZER:', REGULARIZER)
print('STEPS:', STEPS)
print('MOVING_AVERAGE_DECAY:', MOVING_AVERAGE_DECAY)
print('MODEL_SAVE_PATH:', MODEL_SAVE_PATH)
print('MODEL_NAME:', MODEL_NAME)

#BATCH_SIZE = 200
#LEARNING_RATE_BASE = 0.1
#LEARNING_RATE_DECAY = 0.99
#REGULARIZER = 0.0001
#STEPS = 50000
#MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH="./model/"
MODEL_NAME="mnist_model"


def backward(mnist):

    x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
    y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
    y = mnist_forward.forward(x, REGULARIZER)
    global_step = tf.Variable(0, trainable=False)

    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cem = tf.reduce_mean(ce)
    loss = cem + tf.add_n(tf.get_collection('losses'))

    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        mnist.train.num_examples / BATCH_SIZE, 
        LEARNING_RATE_DECAY,
        staircase=True)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())
    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
		       saver.restore(sess, ckpt.model_checkpoint_path)

        for i in range(STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})
            if i % 1000 == 0:
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)


def main():
    mnist = input_data.read_data_sets("./data/", one_hot=True)
    backward(mnist)

if __name__ == '__main__':
    main()


