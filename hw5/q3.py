import numpy as np
from numpy.linalg import norm

# x = x[0], y = x[1], z = x[2]

def f(x):
    F = x[0]**2 + 4*x[1]**2 + 4*x[2]**2 - 16
    return F

def fx(x):
    fx = 2*x[0]
    return fx

def fy(x):
    fy = 8*x[1]
    return fy

def fz(x):
    fz = 8*x[2]
    return fz

def driver():
    x0 = np.array([1,1,1])
    tol = 1e-8
    Nmax = 100
    [xstar,ier,its] = Newton_3d(x0, tol, Nmax)
    print('Xstar: ( ', xstar[0], ' , ', xstar[1], ' , ', xstar[2], ' )')
    print('Error: ', ier)
    print('Iterations: ', its)

def Newton_3d(x0, tol, Nmax):
    xstar = np.zeros(3)
    for its in range(Nmax):
        x1 = np.zeros(3)
        d = f(x0)/(fx(x0)**2 + fy(x0)**2 + fz(x0)**2)
        x1[0] = x0[0] - d*fx(x0)
        x1[1] = x0[1] - d*fy(x0)
        x1[2] = x0[2] - d*fz(x0)
        print('Error at iteration' , its, ' : ', norm(x1-x0))
        if(norm(x1-x0) < tol):
            xstar = x1
            return[xstar, 0, its]
        x0 = x1
    
    xstar = x1
    return[xstar, 1, its]

driver()
