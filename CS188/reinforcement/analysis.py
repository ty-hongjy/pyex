'''
Description: 
Autor: name
Date: 2024-04-23 14:38:15
LastEditors: name
LastEditTime: 2024-05-10 14:41:11
'''
# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.
    return answerDiscount, answerNoise

#折扣系数，表示目的地距离带来的折扣
    # answerDiscount = 0.9
# 意外率，即以某个概率执行意外的行动
    # answerNoise = 0
#生存奖励，其值越低，则Agent更愿意冒风险|
    # answerLivingReward = 0
# 第一种方案的目的是降低奖励值高的节点对Agent的吸引力，
# 并让Agent愿意沿着悬崖前进
def question3a():
    answerDiscount = 0.2 # 0.2 is also OK
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

#第二题的目的是提高掉入悬崖的概率，Agent就会避开悬崖
def question3b():
    answerDiscount = 0.2
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

#第三题的目的是增大最右边奖励值高的节点的吸引力
#并且降低noise,让Agent愿意沿着悬崖前进
def question3c():
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

#第四题的目的同样是增大奖励值最高节点的吸引力
#但是增大Noise,让Agent避开可能调入的悬崖边
def question3d():
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

#第五题的目的是降低所有奖励值节点对Agent的吸引力
#同时要避开悬崖边，所以适当提高Noise值
def question3e():
    answerDiscount = 0
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    return 'NOT POSSIBLE'
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
