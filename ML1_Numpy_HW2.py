import time
from IPython import display

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import sklearn.datasets

np.random.seed(0)
X, y = sklearn.datasets.make_blobs(200, centers=2, cluster_std=0.9)
X[0] += 1.5
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)


def activation(x):
    return np.where(x > 0, 1, 0)


x = np.linspace(-5,5)
plt.plot(x, activation(x))


def perceptron(w, x):
    x_with_bias = np.c_[x, np.ones((len(x), 1))]
    return activation(np.dot(x_with_bias,w))


def plot_decision_boundary(pred_func):
    x_min, x_max = X[:,0].min() - .5, X[:,0].max() + .5
    y_min, y_max = X[:,1].min() - .5, X[:,1].max() + .5
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min,y_max,h))
    z = pred_func(np.c_[xx.ravel(),yy.ravel()])
    z = z.reshape(xx.shape)
    plt.contourf(xx,yy,z,cmap=plt.cm.Spectral)
    plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Spectral)
    plt.show()


w = 2*np.random.random((3,)) - 1
plot_decision_boundary(lambda x: perceptron(w,x))

perceptron(w,X)

w=2*np.random.random((3,))-1
LR=2

for j in range(11):
    pred = perceptron(w,X)

    diff = y-pred
    error = np.mean(np.abs(diff))

    display.clear_output(wait=True)
    plot_decision_boundary(lambda x: perceptron(w,x))
    display.display('Error:'+str(error))
    time.sleep(0.5)

    x_with_bias = np.c_[X, np.ones((len(X), 1))]
    w = w + LR*np.dot(x_with_bias.T, diff)

#answer: 0.045
