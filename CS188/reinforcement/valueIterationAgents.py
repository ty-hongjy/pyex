# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for i in range(self.iterations):
            states=self.mdp.getStates()
            temp_counter = util.Counter( )
            for state in states:
                maxVal = -float('inf')
                for action in self.mdp.getPossibleActions(state):
                    Q = self. computeQValueFromValues(state , action)
                    if Q>maxVal:
                        maxVal = Q
                        temp_counter[state] = maxVal
            self.values = temp_counter
            print(self .values)


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        #第一步，先来实现计算Q-Value的功能
        #把可能的下一-步状态信息进行遍历，并求和
        total = 0
        #按照求Q值的公式，进行代码编写
        for nextState,prob in self.mdp.getTransitionStatesAndProbs(state, action):
            total += prob * (self.mdp.getReward(state, action, nextState)
                + self. discount * self.getValue(nextState))
        return total

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        #初始化
        maxVal = -float('inf')
        bestAction = None
        #对当前状态所有的可能动作进行求Q值的遍历，从中选出最大的Q值作为
        for action in self.mdp.getPossibleActions(state):
            Q = self.computeQValueFromValues(state , action)
            if Q>maxVal:
                maxVal = Q
                bestAction = action
        return bestAction

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        #保存当前MDP状态
        states=self.mdp.getStates()
        for index in range(self.iterations):
            state=states[index % len(states)]
            #接下来只要更新这个state即可，但是题目上要求不更新Terminal节点
            if not self.mdp.isTerminal(state):
                #按照同样的方法求V值
                maxVal = -float('inf')
                for action in self.mdp.getPossibleActions(state):
                    Q = self.computeQValueFromValues(state , action)
                    if Q>maxVal:
                        maxVal = Q
                        #这句话- -定要放在循环内部，防止把某个状态的V值更新成负无穷
                        #这句话更新的是某个单独的节点，而非上面算法中更新了所有节点的V值
                self.values[state] = maxVal


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        #计算所有状态的前驱节点
        predecessors = {}
        #将MPD中的所有state进行遍历
        for state in self.mdp.getStates():
            #接下来只要更新这个state即可，但是题目，上要求不更新Terminal节点
            if not self.mdp.isTerminal(state):
                #按照同样的方法求V值
                maxVal=-float('inf')
                for action in self.mdp.getPossibleActions(state):
                    #为了保存当前节点的前驱节点，必须调用getTransitionStatesAndProbs得到- 系列节点和概率的组合
                    for nextState, prob in self.mdp.getTransitionStatesAndProbs(state,action):
                        #注意，要保存的是前驱节点的信息，所以要以下一个节点作为键值进行索引
                        if nextState in predecessors:
                            predecessors[nextState].add(state)
                        else:
                            predecessors[nextState]={state}

        #初始化一个空的优先级队列
        pq = util.PriorityQueue()

        #对所有非终点的状态s进行遍历
        for s in self.mdp.getStates():
            # maxQ = -float('inf')
            if not self.mdp.isTerminal(s):
                #找到s的V值和最大Q值的差的绝对值diff
                maxQ = -float('inf')
                for action in self .mdp . getPossibleActions(s):
                    Q=self.computeQValueFromValues(s , action)
                    if Q>maxQ:
                        maxQ = Q
                diff = abs(maxQ - self.values[s])
                #把s按照-diff的值,推到优先级队列中
                pq.update(s,-diff)

        #按照迭代次数构造循环
        for _ in range(self. iterations):
            #如果队列为空，则终止循环
            if pq. isEmpty():
                break

            #从队列中弹出一个状态s
            s = pq.pop()

            #更新s的V值
            if not self.mdp.isTerminal(s):
                maxVal = -float('inf')
                for action in self.mdp.getPossibleActions(s):
                    Q=self.computeQValueFromValues(s , action)
                    if Q>maxVal:
                        maxVal = Q

                #这句话更新的是某个单独的节点，而非上面算法中更新了所有节点的V值
                self .values[s]=maxVal

            #立刻遍历s的前驱节点并更新它们的状态
            for p in predecessors[s]:
                #找到p的V值和从p计算的最大Q值的差的绝对值di ff
                maxQ = -float('inf')
                for action in self.mdp.getPossibleActions(p):
                    Q=self.computeQValueFromValues(p , action)
                    if Q>maxQ:
                        maxQ = Q
                        diff = abs(maxQ - self.values[p])

                #如果diff大于theta的值，则将p以-di ff的优先值放到队列中
                if diff>self.theta:
                    pq.update(p, -diff)