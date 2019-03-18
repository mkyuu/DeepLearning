import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.where(x<=0,0,1)

def sigmoid_function(x):
    return 1/(1+np.exp(-x))

def tanh_function(x):
    return np.tanh(x)

def relu_function(x):
    return np.where(x<=0,0,x)

def softmax_function(x):
    return np.exp(x)/np.sum(np.exp(x)) #ソフトマックス関数　分類問題

x = np.linspace(-5,5)
y = x #恒等関数 回帰問題

plt.plot(x,y)
plt.show()