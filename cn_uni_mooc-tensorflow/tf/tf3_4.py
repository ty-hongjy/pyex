#coding:utf-8
#����������磨ȫ���ӣ�

import tensorflow as tf

#��������Ͳ���
#��placeholderʵ�����붨�� ��sess.run��ιһ�����ݣ�
x = tf.placeholder(tf.float32, shape=(1, 2))
w1= tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2= tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))


#����ǰ�򴫲�����
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)


#�ûỰ������
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print("y in tf3_4.py is:\n",sess.run(y, feed_dict={x: [[0.7,0.5]]}))

'''
y in tf3_4.py is:
[[3.0904665]]
'''
))

'''
y in tf3_4.py is:
[[3.0904665]]
'''
