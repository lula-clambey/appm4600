import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt


def driver():
    N = 45

    #h = 2/(N-1)
    f = lambda x: 1/(1+(10*x)**2)
    xi = np.zeros(N)
    for i in range(1,N+1):
        xi[i-1] = np.cos(((2*i-1)*np.pi) / (2*N))
    yi = np.zeros(N)
    for i in range(1,N+1):
        yi[i-1] = f(xi[i-1])
    xgraph = np.linspace(-1,1,1001)
    
    V = evalV(N,xi)
    Vinv = inv(V)
    c = Vinv.dot(yi)
    P = evalP(c,xgraph,N)

    plt.plot(xi,yi,'o')
    plt.plot(xgraph,P)
    plt.grid(True)
    plt.show()

    #plt.plot(xgraph, f(xgraph))
    #plt.grid(True)
    #plt.show()


def evalV(N,xi):
    V = np.zeros((N,N))

    for j in range(1,N+1):
        for k in range(1,N+1):
            V[k-1,j-1] = xi[k-1]**(N-j)
    return V

def evalP(c,xgraph,N):
    P = np.zeros(len(xgraph))
    for i in range(1,N+1):
        P += c[i-1]*xgraph**(N-i)
    return P

driver()