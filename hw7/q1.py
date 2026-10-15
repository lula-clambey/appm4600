import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt


def driver():
    N = 15

    h = 2/(N-1)
    f = lambda x: 1/(1+(10*x)**2)
    xi = np.zeros(N)
    for i in range(1,N+1):
        xi[i-1] = -1 + (i-1)*h
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

"""
def driver():
    f = lambda x: 1/(1+(10*x)**2)
    N = 10
    a = 0
    b = 1
    ''' Create interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    # print('xint =',xint)
    '''Create interpolation data'''
    yint = f(xint)
    # print('yint =',yint)
    ''' Create the Vandermonde matrix'''
    V = Vandermonde(xint,N)
    # print('V = ',V)
    ''' Invert the Vandermonde matrix'''
    Vinv = inv(V)
    # print('Vinv = ' , Vinv)
    ''' Apply inverse to rhs'''
    ''' to create the coefficients'''
    coef = Vinv @ yint
    # print('coef = ', coef)
    # No validate the code
    Neval = 100
    xeval = np.linspace(a,b,Neval+1)
    yeval = eval_monomial(xeval,coef,N,Neval)
    # exact function
    yex = f(xeval)
    err = norm(yex-yeval)
    print('err = ', err)
    return

def eval_monomial(xeval,coef,N,Neval):
    yeval = coef[0]*np.ones(Neval+1)
    # print('yeval = ', yeval)
    for j in range(1,N+1):
        for i in range(Neval+1):
        # print('yeval[i] = ', yeval[i])
        # print('a[j] = ', a[j])
        # print('i = ', i)
        # print('xeval[i] = ', xeval[i])
            yeval[i] = yeval[i] + coef[j]*xeval[i]**j
    return yeval

def Vandermonde(xint,N):
    V = np.zeros((N+1,N+1))
    ''' fill the first column'''
    for j in range(N+1):
        V[j][0] = 1.0
    for i in range(1,N+1):
        for j in range(N+1):
            V[j][i] = xint[j]**i
    return V

driver()
"""