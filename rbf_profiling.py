from math import exp
import numpy as np
from scipy.interpolate import Rbf

@profile
def rbf_network(X, beta, theta):

    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y

@profile
def rbf_scipy(X, beta):

    N = X.shape[0]
    D = X.shape[1]    
    rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    #Xtuple = tuple([X[:, i] for i in range(D)])
    Xtuple = tuple([X[:, i] for i in range(D)])

    return rbf(*Xtuple)