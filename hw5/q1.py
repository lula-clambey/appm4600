import numpy as np
from numpy.linalg import norm
from numpy.linalg import inv

def driver():

    x0 = np.array([1,1])
    tol = 1e-8
    Nmax = 100
    [xstar, ier, it] = Newton_approx(x0, tol, Nmax)
    print('Method 1')
    print('Xstar: ', xstar)
    print('Error: ', ier)
    print('Iterations: ', it)

    [xstar, ier, it] = Newton(x0, tol, Nmax)
    print('Method 2')
    print('Xstar: ', xstar)
    print('Error: ', ier)
    print('Iterations: ', it)

def evalF(x):
    F = np.zeros(2)
    F[0] = 3*x[0]**2 - x[1]**2
    F[1] = 3*x[0]*x[1]**2 - x[0]**3 - 1
    return F

def evalJ(x):
    J = np.array([[6*x[0], -2*x[1]],[3*x[1]**2 - 3*x[0]**2, 6*x[0]*x[1]]])
    return J

def Newton_approx(x0, tol, Nmax):

    J = np.array([[1/6, 1/18], [0, 1/6]])

    for its in range(Nmax):
        F = evalF(x0)
        x1 = x0 - J.dot(F)
        if(norm(x1 - x0) < tol):
            xstar = x1
            ier = 0
            return[xstar, ier, its]
        x0 = x1

    xstar = x1
    ier = 1
    return[xstar, ier, its]

def Newton(x0, tol, Nmax):

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
    return[xstar,ier,its]

driver()

