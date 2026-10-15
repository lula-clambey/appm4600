import numpy as np
import time
from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    x0 = np.array([-0.5, 0.25])
    Nmax = 100
    tol = 1e-4

    t = time.time()
    for j in range(50):
        [xstar,ier,its] = fixedPt(x0,tol,Nmax)
        elapsed = time.time()-t
    print(xstar)
    print('Fixed pt: the error message reads:',ier)
    print('Fixed pt: took this many seconds:',elapsed/50)
    print('Fixed pt: number of iterations is:',its)

    t = time.time()
    for j in range(50):
        [xstar,ier,its] = Newton(x0,tol,Nmax)
        elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier)
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)

def evalF(x):
    F = np.zeros(2)
    F[0] = 3*x[0]**2 + 4*x[1]**2 - 1
    F[1] = x[1]**3 - 8*x[0]**3 - 1
    return F

def evalJ(x):
    J = np.array([[6*x[0], 8*x[1]],[-24*x[0]**2, 3*x[1]**2]])
    return J

def fixedPt(x0,tol,Nmax):
    GJ = np.array([[0.016, -0.17], [0.52, -0.26]])
    for its in range(Nmax):
        F = evalF(x0)
        x1 = x0 - GJ.dot(F)
        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier, its]
        x0 = x1
    xstar = x1
    ier = 1
    return[xstar,ier,its]

def Newton(x0,tol,Nmax):
    for its in range(Nmax):
        J = evalJ(x0)
        Jinv = inv(J)
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier, its]
        x0 = x1
    xstar = x1
    ier = 1
    return[xstar, ier, its]

driver()
