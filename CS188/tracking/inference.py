# inference.py
# ------------
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


import itertools
import random
import busters
import game

from util import manhattanDistance, raiseNotDefined


class DiscreteDistribution(dict):
    """
    A DiscreteDistribution models belief distributions and weight distributions
    over a finite set of discrete keys.
    """
    def __getitem__(self, key):
        self.setdefault(key, 0)
        return dict.__getitem__(self, key)

    def copy(self):
        """
        Return a copy of the distribution.
        """
        return DiscreteDistribution(dict.copy(self))

    def argMax(self):
        """
        Return the key with the highest value.
        """
        if len(self.keys()) == 0:
            return None
        all = list(self.items())
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        return all[maxIndex][0]

    def total(self):
        """
        Return the sum of values for all keys.
        """
        return float(sum(self.values()))

    def normalize(self):
        """
        Normalize the distribution such that the total value of all keys sums
        to 1. The ratio of values for all keys will remain the same. In the case
        where the total value of the distribution is 0, do nothing.

        >>> dist = DiscreteDistribution()
        >>> dist['a'] = 1
        >>> dist['b'] = 2
        >>> dist['c'] = 2
        >>> dist['d'] = 0
        >>> dist.normalize()
        >>> list(sorted(dist.items()))
        [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
        >>> dist['e'] = 4
        >>> list(sorted(dist.items()))
        [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
        >>> empty = DiscreteDistribution()
        >>> empty.normalize()
        >>> empty
        {}
        """
        "*** YOUR CODE HERE ***"
        #要进行归-化,首先需要求总体样本数量total
        total = self.total()
        #根据注释的提醒，total为0的时候不要做任何事情
        if total!=0:
            for k,v in self.items():
                self[k] = v/total

    def sample(self):
        """
        Draw a random sample from the distribution and return the key, weighted
        by the values associated with each key.

        >>> dist = DiscreteDistribution()
        >>> dist['a'] = 1
        >>> dist['b'] = 2
        >>> dist['c'] = 2
        >>> dist['d'] = 0
        >>> N = 100000.0
        >>> samples = [dist.sample() for _ in range(int(N))]
        >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
        0.2
        >>> round(samples.count('b') * 1.0/N, 1)
        0.4
        >>> round(samples.count('c') * 1.0/N, 1)
        0.4
        >>> round(samples.count('d') * 1.0/N, 1)
        0.0
        """
        "*** YOUR CODE HERE ***"
        #当0<=u<0.2,则返回'a',当0.2<=u<0.6,则返回'b',当0.6<=u<1，则返回'c'
        u=random.random( )
        #使用变量alpha表示区间的下限
        alpha = 0.0
        for key,value in self.items():
            #只有当随机数u落在了指定的离散分布区间内，才会返回对应的key即样本
            if alpha <= u < alpha+(value/self.total()):
                return key
            #为了得到下一个分布的区间下限，我们需要不断地更新alpha
            alpha += value/self.total()

class InferenceModule:
    """
    An inference module tracks a belief distribution over a ghost's location.
    """
    ############################################
    # Useful methods for all inference modules #
    ############################################

    def __init__(self, ghostAgent):
        """
        Set the ghost agent for later access.
        """
        self.ghostAgent = ghostAgent
        self.index = ghostAgent.index
        self.obs = []  # most recent observation position

    def getJailPosition(self):
        return (2 * self.ghostAgent.index - 1, 1)

    def getPositionDistributionHelper(self, gameState, pos, index, agent):
        try:
            jail = self.getJailPosition()
            gameState = self.setGhostPosition(gameState, pos, index + 1)
        except TypeError:
            jail = self.getJailPosition(index)
            gameState = self.setGhostPositions(gameState, pos)
        pacmanPosition = gameState.getPacmanPosition()
        ghostPosition = gameState.getGhostPosition(index + 1)  # The position you set
        dist = DiscreteDistribution()
        if pacmanPosition == ghostPosition:  # The ghost has been caught!
            dist[jail] = 1.0
            return dist
        pacmanSuccessorStates = game.Actions.getLegalNeighbors(pacmanPosition, \
                gameState.getWalls())  # Positions Pacman can move to
        if ghostPosition in pacmanSuccessorStates:  # Ghost could get caught
            mult = 1.0 / float(len(pacmanSuccessorStates))
            dist[jail] = mult
        else:
            mult = 0.0
        actionDist = agent.getDistribution(gameState)
        for action, prob in actionDist.items():
            successorPosition = game.Actions.getSuccessor(ghostPosition, action)
            if successorPosition in pacmanSuccessorStates:  # Ghost could get caught
                denom = float(len(actionDist))
                dist[jail] += prob * (1.0 / denom) * (1.0 - mult)
                dist[successorPosition] = prob * ((denom - 1.0) / denom) * (1.0 - mult)
            else:
                dist[successorPosition] = prob * (1.0 - mult)
        return dist

    def getPositionDistribution(self, gameState, pos, index=None, agent=None):
        """
        Return a distribution over successor positions of the ghost from the
        given gameState. You must first place the ghost in the gameState, using
        setGhostPosition below.
        """
        if index == None:
            index = self.index - 1
        if agent == None:
            agent = self.ghostAgent
        return self.getPositionDistributionHelper(gameState, pos, index, agent)

    def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
        """
        Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
        """
        "*** YOUR CODE HERE ***"
        # raiseNotDefined()
        #根据题目描述，需要判定鬼怪是否已经被送到jail中
        if ghostPosition == jailPosition:
            #该分支表示鬼怪在监狱中，即noisyDistance为None的概率为100%
            if noisyDistance is None:
                return 1.0
            #该分支表示鬼怪在监狱中，即noisyDistance不为None的概率为0%
            else:
                return 0.0
        else:
            if noisyDistance is None:
                return 0.0
            else:
                return busters.getObservationProbability(noisyDistance, manhattanDistance(pacmanPosition, ghostPosition))

    def setGhostPosition(self, gameState, ghostPosition, index):
        """
        Set the position of the ghost for this inference module to the specified
        position in the supplied gameState.

        Note that calling setGhostPosition does not change the position of the
        ghost in the GameState object used for tracking the true progression of
        the game.  The code in inference.py only ever receives a deep copy of
        the GameState object which is responsible for maintaining game state,
        not a reference to the original object.  Note also that the ghost
        distance observations are stored at the time the GameState object is
        created, so changing the position of the ghost will not affect the
        functioning of observe.
        """
        conf = game.Configuration(ghostPosition, game.Directions.STOP)
        gameState.data.agentStates[index] = game.AgentState(conf, False)
        return gameState

    def setGhostPositions(self, gameState, ghostPositions):
        """
        Sets the position of all ghosts to the values in ghostPositions.
        """
        for index, pos in enumerate(ghostPositions):
            conf = game.Configuration(pos, game.Directions.STOP)
            gameState.data.agentStates[index + 1] = game.AgentState(conf, False)
        return gameState

    def observe(self, gameState):
        """
        Collect the relevant noisy distance observation and pass it along.
        """
        distances = gameState.getNoisyGhostDistances()
        if len(distances) >= self.index:  # Check for missing observations
            obs = distances[self.index - 1]
            self.obs = obs
            self.observeUpdate(obs, gameState)

    def initialize(self, gameState):
        """
        Initialize beliefs to a uniform distribution over all legal positions.
        """
        self.legalPositions = [p for p in gameState.getWalls().asList(False) if p[1] > 1]
        self.allPositions = self.legalPositions + [self.getJailPosition()]
        self.initializeUniformly(gameState)

    ######################################
    # Methods that need to be overridden #
    ######################################

    def initializeUniformly(self, gameState):
        """
        Set the belief state to a uniform prior belief over all positions.
        """
        raise NotImplementedError

    def observeUpdate(self, observation, gameState):
        """
        Update beliefs based on the given distance observation and gameState.
        """
        raise NotImplementedError

    def elapseTime(self, gameState):
        """
        Predict beliefs for the next time step from a gameState.
        """
        raise NotImplementedError

    def getBeliefDistribution(self):
        """
        Return the agent's current belief state, a distribution over ghost
        locations conditioned on all evidence so far.
        """
        raise NotImplementedError


class ExactInference(InferenceModule):
    """
    The exact dynamic inference module should use forward algorithm updates to
    compute the exact belief function at each time step.
    """
    def initializeUniformly(self, gameState):
        """
        Begin with a uniform distribution over legal ghost positions (i.e., not
        including the jail position).
        """
        self.beliefs = DiscreteDistribution()
        for p in self.legalPositions:
            self.beliefs[p] = 1.0
        self.beliefs.normalize()

    def observeUpdate(self, observation, gameState):
        """
        Update beliefs based on the distance observation and Pacman's position.

        The observation is the noisy Manhattan distance to the ghost you are
        tracking.

        self.allPositions is a list of the possible ghost positions, including
        the jail position. You should only consider positions that are in
        self.allPositions.

        The update model is not entirely stationary: it may depend on Pacman's
        current position. However, this is not a problem, as Pacman's current
        position is known.
        """
        "*** YOUR CODE HERE ***"
        # raiseNotDefined()
        #获取旧的置信度网络数据
        oldPD = self.beliefs
        #获取吃豆人的位置
        pacmanPosition = gameState.getPacmanPosition()
        #获得当前地图中监狱的位置
        jailPosition = self.getJailPosition()
        #建立新的离散分布对象以存储新的置信度网络数据
        newPD = DiscreteDistribution()
        #遍历所有鬼怪可能出现的位置
        for ghostPosition in self.allPositions:
            newPD[ghostPosition] = self.getObservationProb(observation, pacmanPosition, ghostPosition, jailPosition)*oldPD[ghostPosition]
        #将新的置信度网络更新到self.beliefs中
        self.beliefs=newPD
        self.beliefs.normalize()

    def elapseTime(self, gameState):
        """
        Predict beliefs in response to a time step passing from the current
        state.

        The transition model is not entirely stationary: it may depend on
        Pacman's current position. However, this is not a problem, as Pacman's
        current position is known.
        """
        "*** YOUR CODE HERE ***"
        # 获取旧的置信度网络数据（其实就是一个离散分布)
        oldPD = self.beliefs
        # 获取吃豆人的位置
        pacmanPosition=gameState.getPacmanPosition()
        jailPosition=self.getJailPosition()
        # 建立新的离散分布对象以存储新的置信度网络数据
        newPD = DiscreteDistribution()
        # 遍历所有鬼怪所有可能出现的位置，格每一个可能出现的位置都作为初始位置进行汁算
        for oldPos in self.allPositions:
            # 根据Time Elapse算法内容，我们得到接下来鬼怪可能存在位置的离散分布
            newPosDist= self.getPositionDistribution(gameState, oldPos)
            # 新的置信度期络中的数据需要格所有从oldPos出发达到newPos的可能性进行累加
            for newPos in self.allPositions:
                # 考虑到从oldPos到达newPos的概率可能为0，我们可以在这里做一些优化
                if newPosDist[newPos]>0:
                    newPD[newPos] += newPosDist[newPos]*oldPD[oldPos]
        # 将新的置信度网络更新到self.beliefs中
        self.beliefs = newPD
        # 最后置信度网络讲行归一化
        self.beliefs.normalize()

    def getBeliefDistribution(self):
        return self.beliefs


class ParticleFilter(InferenceModule):
    """
    A particle filter for approximately tracking a single ghost.
    """
    def __init__(self, ghostAgent, numParticles=300):
        InferenceModule.__init__(self, ghostAgent)
        self.setNumParticles(numParticles)

    def setNumParticles(self, numParticles):
        self.numParticles = numParticles

    def initializeUniformly(self, gameState):
        """
        Initialize a list of particles. Use self.numParticles for the number of
        particles. Use self.legalPositions for the legal board positions where
        a particle could be located. Particles should be evenly (not randomly)
        distributed across positions in order to ensure a uniform prior. Use
        self.particles for the list of particles.
        """
        self.particles = []
        "*** YOUR CODE HERE ***"
        # 所谓的初始化，就是将一堆粒子放到给定的空间中
        # 假设空间范團为[1,10〕，现在有1000个粒子，如果平均分布，那么1到10各取100次就是这个采样分布，形如：
        # [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,...7,8,9,10,1,2,3,4,5,6,7,8,9,101
        self.particles += self.legalPositions*(self.numParticles//len(self.legalPositions))
        # 还要考虑特殊情况：粒子总数不能整除空间尺寸，比如空间范国为[1,101，但是粒子数量为95
        self.particles += self.legalPositions[:(self.numParticles%len(self.legalPositions))]

    def observeUpdate(self, observation, gameState):
        """
        Update beliefs based on the distance observation and Pacman's position.

        The observation is the noisy Manhattan distance to the ghost you are
        tracking.

        There is one special case that a correct implementation must handle.
        When all particles receive zero weight, the list of particles should
        be reinitialized by calling initializeUniformly. The total method of
        the DiscreteDistribution may be useful.
        """
        "*** YOUR CODE HERE ***"
        # 获取吃豆人的位費
        pacmanPosition = gameState.getPacmanPosition()
        # 获得当前地图中监戒的位置
        jailPosition = self.getJailPosition()
        # 建立新的离散分布对系以存储新的置信度网络数据
        newPD = DiscreteDistribution()
        # 本算法通过观聚样本粒子的概率，更新置信度网络中的数据
        for particle in self. particles:
            newPD[particle] += self.getObservationProb(observation, pacmanPosition, particle, jailPosition)
        # 根据注释的提示，需要考虑特殊情况，即置所有粒子的概率总和为0，就调用初始化方法
        if newPD.total()==0:
            self.initializeUniformly(gameState)
        else:
            # 将新的置信度网络更新到self.beliefs中
            self.beliefs = newPD
            # 最后，将置信度网络进行归一化
            self.beliefs.normalize()
            #再次生成新的样本粒子（因为置信发网络中的数据发生了变化，所以必须重新米样，以计算新的置信度网络）
            self.particles = [self.beliefs.sample() for _ in range(self.numParticles)]

    def elapseTime(self, gameState):
        """
        Sample each particle's next state based on its current state and the
        gameState.
        """
        "*** YOUR CODE HERE ***"
        PosDist={}
        # 近似推理没有self.beliefs属性，所有的概率需用通过粒子来计算，所以我们只需要便新粒千数据即可
        # 更新粒子数据的方法，就是从旧的粒子数据中衍生出新的粒子数据
        for index, particle in enumerate(self.particles):
            # 在项目说明中提示我们要降低对self.getPositionDistribution的调用次数
            # 为了达到上述目的，我们预先设置一个以particle为键的宇典，值为该particle对应的PositionDistribution
            if particle not in PosDist.keys():
                newPosDist = self.getPositionDistribution(gameState, particle)
                PosDist[particle] = newPosDist
            # 接着，我们就可以直接使用字典PosDist中的己经计算好的PositionDistribution数据
            newParticle = PosDist[particle].sample()
            self.particles[index] = newParticle

    def getBeliefDistribution(self):
        """
        Return the agent's current belief state, a distribution over ghost
        locations conditioned on all evidence and time passage. This method
        essentially converts a list of particles into a belief distribution.
        
        This function should return a normalized distribution.
        """
        "*** YOUR CODE HERE ***"
        # 构造商散分布对象用于存放概率分布
        belief = DiscreteDistribution()
        # 接着只需要对以粒子为键的宇典对象进行＋1计数，即可得到每一个粒子出现的次数
        for particle in self.particles:
            belief[particle] += 1
        belief.normalize()
        return belief

class JointParticleFilter(ParticleFilter):
    """
    JointParticleFilter tracks a joint distribution over tuples of all ghost
    positions.
    """
    def __init__(self, numParticles=600):
        self.setNumParticles(numParticles)

    def initialize(self, gameState, legalPositions):
        """
        Store information about the game, then initialize particles.
        """
        self.numGhosts = gameState.getNumAgents() - 1
        self.ghostAgents = []
        self.legalPositions = legalPositions
        self.initializeUniformly(gameState)

    def initializeUniformly(self, gameState):
        """
        Initialize particles to be consistent with a uniform prior. Particles
        should be evenly distributed across positions in order to ensure a
        uniform prior.
        """
        self.particles = []
        "*** YOUR CODE HERE ***"
        # 所谓联合采样，就是采样空间中的数据，不再是一个单独的值，而是若干数据的组合
        # 假设有4个鬼怪，则采样数据中的每一个元素都将会是一个四元组
        # itertools.product的第一个参数表示取值范国，参败repeat表示元组中的元奏数量
        permutations = list(itertools.product(self.legalPositions, repeat=self.numGhosts))
        # 题目要求打乱上述排列中的内容，以得到一个乱序的采样空间
        random.shuffle(permutations)
        # 所谓的初始化，就是将一堆粒子放到给定的采样空间(即permutations)中
        self.particles += permutations*(self.numParticles//len(permutations))
        # 还要考虑特殊情况：粒子总数不能整除空问尺寸，比如空间范国为[1,10]，但是粒子数量为95
        self.particles += permutations[:(self.numParticles%len(permutations))]

    def addGhostAgent(self, agent):
        """
        Each ghost agent is registered separately and stored (in case they are
        different).
        """
        self.ghostAgents.append(agent)

    def getJailPosition(self, i):
        return (2 * i + 1, 1)

    def observe(self, gameState):
        """
        Resample the set of particles using the likelihood of the noisy
        observations.
        """
        observation = gameState.getNoisyGhostDistances()
        self.observeUpdate(observation, gameState)

    def observeUpdate(self, observation, gameState):
        """
        Update beliefs based on the distance observation and Pacman's position.

        The observation is the noisy Manhattan distances to all ghosts you
        are tracking.

        There is one special case that a correct implementation must handle.
        When all particles receive zero weight, the list of particles should
        be reinitialized by calling initializeUniformly. The total method of
        the DiscreteDistribution may be useful.
        """
        "*** YOUR CODE HERE ***"
       # 获取吃豆人的位置
        pacmanPosition=gameState.getPacmanPosition()
        # 建立新的商散分布对象以存储新的置信度网络数据
        newPD = DiscreteDistribution()
        # 本算法通过观察样本样本的概率，以更新置信度网络中的数据
        for particle in self.particles:
        # 利用眾乘算法，求出在该位置4个鬼怪都存在的橛率
            prob = 1
            for i in range(self.numGhosts):
                prob *=  self.getObservationProb(observation[i], pacmanPosition, particle[i], self.getJailPosition(i))
            newPD[particle] += prob
        # 根据注释的提示，需要考處特殊情况，即買所有粒子的概率总和为0，就调用初始化方法
        if newPD.total()==0:
            self.initializeUniformly(gameState)
        else:
            # 最后，将置信度网络进行归一化
            newPD.normalize()
            # 再次生成新的样本粒子(因为買信度网络中的数据发生了变化，所以必须重新采样，以计算新的置信度网络)
            self.particles = [newPD.sample() for _ in range(self.numParticles)]

    def elapseTime(self, gameState):
        """
        Sample each particle's next state based on its current state and the
        gameState.
        """
        newParticles = []
        for oldParticle in self.particles:
            newParticle = list(oldParticle)  # A list of ghost positions

            # now loop through and update each entry in newParticle...
            "*** YOUR CODE HERE ***"
            for i in range(self.numGhosts):
                newPosDist = self.getPositionDistribution(gameState, newParticle, i, self.ghostAgents[i])
                newParticle[i] = newPosDist.sample()

            """*** END YOUR CODE HERE ***"""
            newParticles.append(tuple(newParticle))
        self.particles = newParticles


# One JointInference module is shared globally across instances of MarginalInference
jointInference = JointParticleFilter()


class MarginalInference(InferenceModule):
    """
    A wrapper around the JointInference module that returns marginal beliefs
    about ghosts.
    """
    def initializeUniformly(self, gameState):
        """
        Set the belief state to an initial, prior value.
        """
        if self.index == 1:
            jointInference.initialize(gameState, self.legalPositions)
        jointInference.addGhostAgent(self.ghostAgent)

    def observe(self, gameState):
        """
        Update beliefs based on the given distance observation and gameState.
        """
        if self.index == 1:
            jointInference.observe(gameState)

    def elapseTime(self, gameState):
        """
        Predict beliefs for a time step elapsing from a gameState.
        """
        if self.index == 1:
            jointInference.elapseTime(gameState)

    def getBeliefDistribution(self):
        """
        Return the marginal belief over a particular ghost by summing out the
        others.
        """
        jointDistribution = jointInference.getBeliefDistribution()
        dist = DiscreteDistribution()
        for t, prob in jointDistribution.items():
            dist[t[self.index - 1]] += prob
        return dist
