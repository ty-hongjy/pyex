import nn

class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        #根据线性代数的基础知识，当x=(1,2,3), 与w发生相乘的结果就是两者的点积
        return nn.DotProduct(self.w,x)

    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        if nn.as_scalar(self.run(x))>=0:
            return 1
        else:
            return -1

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        #本题中的训练过程要求精确度为100%，即数据集中所有x预测结果，必须和样本中的y保持- -致
        #所以，我们可以构造一个死循环，不断地使用数据集中的(x , y)来训练我们的模型
        sholdStop = False
        while not sholdStop:
            #在循环中不断获取(x ,y)进行训练
            for x, y in dataset.iterate_once(batch_size=1):
                if not self.get_prediction(x) == nn.as_scalar(y):
                    self.w.update(x, nn.as_scalar(y))
                    #下方的break表示当前的预测值和y不- -样，所以需要从头再开始训练
                    break
            #如果能执行到else分支中的语句，表示所有的预测值都已经和y-致了!
            else:
            #为了能让外层循环停下来，我们构造-一个标志变量
                sholdStop = True

class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.layer_size=200
        #如果bathc_ size为1，表示每一次只用一组数据进行训练，那么带来的问题就是效率非常低下
        # self.batch_size = 1
        # self.learning_rate = 0.05
        # self.layer_number = 2

        self.batch_size = 100
        self.learning_rate = 0.05
        self.layer_number = 3

        #构造参数W和b的集合
        self.W =[]
        self.b =[]

        #根据隐藏层的数量，初始化W和b的内容，特别注意W和b的类型是不一样的!
        for i in range(self.layer_number):
            if i==0:
                #第一层神经网络的输入数据为x，此题中x的size为1
                self.W.append(nn.Parameter(1,self.layer_size))
                self.b.append(nn.Parameter(1,self.layer_size))
            elif i==self.layer_number-1:
                #最后一层神经网络的输出数据为y,此题中y的size为1
                self.W.append(nn.Parameter(self.layer_size,1))
                self.b.append(nn.Parameter(1,1))
            else:
                #既不是第一层，也不是最后一层的神经网络，他们的输入和输出参数和相邻层次有关
                self.W.append(nn.Parameter(self.layer_size , self.layer_size))
                self.b.append(nn.Parameter(1, self.layer_size))

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        #构造一个专门存储输入数据的变量，初始值为x
        input_data = x
        #依然根据隐藏层的数量，构造循环
        for i in range(self.layer_number):
            #参考线性规划的代码，构造循环体
            fx = nn.Linear(input_data, self.W[i])
            output_data = nn.AddBias(fx, self.b[i])
            #根据提示，最后一层神经网络则无需调用激活函数
            if i==self.layer_number - 1:
                predicted_y = output_data
            else:
            #如果不是最后一层神经网络，则调用激活函数，计算下一层的输入数据
                input_data =nn.ReLU(output_data)
        return predicted_y

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        predicted_y = self.run(x)
        return nn.SquareLoss(predicted_y, y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        #构造存储损失值的变量，在没有达到题目要求的损失精度之前，一直循环
        loss_number = float('inf')
        while loss_number>=0.02:
            #从数据集中获取(x,y)的组合作为训练数据
            for (x,y) in dataset.iterate_once(self.batch_size):
                #计算损失值
                loss=self.get_loss(x,y)
                print(type(loss))
                # loss = float(loss)
                print(type(loss))
                loss_number = nn.as_scalar(loss)
                #构造梯度下降算法的实现
                grad_wrt = nn.gradients(loss, self.W + self.b)
                #遍历grad_ _wrt中的参数，进行更新
                for i in range(self.layer_number):
                    self.W[i].update(grad_wrt[i], -self.learning_rate)
                    self.b[i].update(grad_wrt[len(self.W)+i],-self.learning_rate)

class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.layer_size=200
        #如果bathc_ size为1，表示每一次只用一组数据进行训练，那么带来的问题就是效率非常低下
        # self.batch_size = 1
        # self.learning_rate = 0.05
        # self.layer_number = 2

        self.batch_size = 500
        self.learning_rate = 0.3
        self.layer_number = 3

        #构造参数W和b的集合
        self.W =[]
        self.b =[]

        #根据隐藏层的数量，初始化W和b的内容，特别注意W和b的类型是不一样的!
        for i in range(self.layer_number):
            if i==0:
                #第一层神经网络的输入数据为x，此题中x的size为1
                self.W.append(nn.Parameter(784,self.layer_size))
                self.b.append(nn.Parameter(1,self.layer_size))
            elif i==self.layer_number-1:
                #最后一层神经网络的输出数据为y,此题中y的size为10
                self.W.append(nn.Parameter(self.layer_size,10))
                self.b.append(nn.Parameter(1,10))
            else:
                #既不是第一层，也不是最后一层的神经网络，他们的输入和输出参数和相邻层次有关
                self.W.append(nn.Parameter(self.layer_size , self.layer_size))
                self.b.append(nn.Parameter(1, self.layer_size))

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        #构造一个专门存储输入数据的变量，初始值为x
        input_data = x
        #依然根据隐藏层的数量，构造循环
        for i in range(self.layer_number):
            #参考线性规划的代码，构造循环体
            fx = nn.Linear(input_data, self.W[i])
            output_data = nn.AddBias(fx, self.b[i])
            #根据提示，最后一层神经网络则无需调用激活函数
            if i==self.layer_number - 1:
                predicted_y = output_data
            else:
            #如果不是最后一层神经网络，则调用激活函数，计算下一层的输入数据
                input_data =nn.ReLU(output_data)
        return predicted_y

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        #特别注意,本题中的损失函数和上一题不- -样!
        predicted_y = self.run(x)
        return nn.SoftmaxLoss(predicted_y, y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        #构造用于存放精确度的变量，在没有达到题目要求的精确度之前，一直循环
        accuracy = 0
        while accuracy<=0.975:
            #从数据集中获取(x,y)的组合作为训练数据
            for (x,y) in dataset.iterate_once(self.batch_size):
                #计算损失值
                loss=self.get_loss(x,y)
                #构造梯度下降算法的实现
                grad_wrt = nn.gradients(loss, self.W + self.b)
                #遍历grad_wrt中的参数，进行更新
                for i in range(self.layer_number):
                    self.W[i].update(grad_wrt[i], -self.learning_rate)
                    self.b[i].update(grad_wrt[len(self.W)+i],-self.learning_rate)
            #数据集轮询一遍之后，更新精确度变量
            accuracy=dataset.get_validation_accuracy()
            print("Accuracy:",accuracy)

class LanguageIDModel(object):
    """
    A model for language identification at a single-word granularity.

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Our dataset contains words from five different languages, and the
        # combined alphabets of the five languages contain a total of 47 unique
        # characters.
        # You can refer to self.num_chars or len(self.languages) in your code
        self.num_chars = 47
        self.languages = ["English", "Spanish", "Finnish", "Dutch", "Polish"]

        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"

    def run(self, xs):
        """
        Runs the model for a batch of examples.

        Although words have different lengths, our data processing guarantees
        that within a single batch, all words will be of the same length (L).

        Here `xs` will be a list of length L. Each element of `xs` will be a
        node with shape (batch_size x self.num_chars), where every row in the
        array is a one-hot vector encoding of a character. For example, if we
        have a batch of 8 three-letter words where the last word is "cat", then
        xs[1] will be a node that contains a 1 at position (7, 0). Here the
        index 7 reflects the fact that "cat" is the last word in the batch, and
        the index 0 reflects the fact that the letter "a" is the inital (0th)
        letter of our combined alphabet for this task.

        Your model should use a Recurrent Neural Network to summarize the list
        `xs` into a single node of shape (batch_size x hidden_size), for your
        choice of hidden_size. It should then calculate a node of shape
        (batch_size x 5) containing scores, where higher scores correspond to
        greater probability of the word originating from a particular language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
        Returns:
            A node with shape (batch_size x 5) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"

    def get_loss(self, xs, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 5). Each row is a one-hot vector encoding the correct
        language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
            y: a node with shape (batch_size x 5)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
