import numpy as np

def driver():
    f = lambda x: np.e**(3*x) - 27*x**6 +27*x**4*np.e**x - 9*x**2*np.e**(2*x)
    fp = lambda x: 3*np.e**(3*x) - 162*x**5 + 27*(4*x**3*np.e**x + np.e**x*x**4) - 9*(2*x*np.e**(2*x) + np.e**(2*x)*2*x**2)   

    p0 = 4
    tol = 1e-8
    Nmax = 100
    m = 3
    [pstar, it, ier] = newton(f,fp,p0,tol,Nmax)
    print('1) P* = ', pstar)
    print('Iterations: ', it)
    print('Error: ', ier)

    [pstar, it, ier] = newton_mod_m(f,fp,p0,m,tol,Nmax)
    print('2) P* = ', pstar)
    print('Iterations: ', it)
    print('Error: ', ier)

    [pstar, it, ier] = newton_mod_x(f,fp,p0,tol,Nmax)
    print('3) P* = ', pstar)
    print('Iterations: ', it)
    print('Error: ', ier)

def newton(f,fp,p0,tol,Nmax):
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0) 
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [pstar, it,info]
        p0 = p1

    pstar = p1
    info = 1
    return [pstar, it, info]

def newton_mod_m(f,fp,p0,m,tol,Nmax):
    for it in range(Nmax):
        p1 = p0-m*(f(p0)/fp(p0)) 
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [pstar, it, info]
        p0 = p1

    pstar = p1
    info = 1
    return [pstar, it, info]

def newton_mod_x(f,fp,p0,tol,Nmax):
    for it in range(Nmax):
        p1 = f(p0)/fp(p0) 
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [pstar, it, info]
        p0 = p1

    pstar = p1
    info = 1
    return [pstar, it, info]


driver()