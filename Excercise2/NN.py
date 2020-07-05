import numpy as np

X=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]),dtype=float)
y=np.array(([0],[1],[1],[0]),dtype=float)

def segmoid(t):
    return 1/(1+np.exp(-t))

def sigmoid_derivative(p):
    return p * (1-p)

class NNetwork:
    def __init__(self,x,y):
        self.input = x
        self.weights1=np.random.rand(3,4)
        self.bias1=np.random.rand(4,1)
        self.weights2=np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(self.y.shape)
    
    def feedforward(self):
        self.layer1=segmoid(np.dot(self.input,self.weights1))
        self.layer2=segmoid(np.dot(self.layer1,self.weights2))
        return self.layer2
    
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2*(self.y -self.output)*sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2*(self.y -self.output)*sigmoid_derivative(self.output), self.weights2.T)*sigmoid_derivative(self.layer1))

        self.weights1 += d_weights1
        self.weights2 += d_weights2
    
    def train(self,x,y):
        self.output = self.feedforward()
        self.backprop()

nn = NNetwork(X,y)
for i in range(1000):
    nn.train(X,y)
    if i%100 == 0:   
        print("iteration" + str(i) +"\n")
        print("input \n"+str(X))
        print("expected output \n"+str(y))
        print("actual output \n"+ str(nn.output))
        print("loss \n"+str(np.mean(np.square(y-nn.output))))
    
    
    
