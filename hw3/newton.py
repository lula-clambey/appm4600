# import libraries
import numpy as np
def driver():
    f = lambda x: x(1+((7-x**5)/x**2))**3
    fp = lambda x: -3*x*(1+((7-x**5)/x**2))**2*(14*x**-2 + 3*x**2)
    p0 = 1.0
    f = lambda x: (x-2)*(x-5)*np.exp(x)
    fp = lambda x: (x-2)*(x-5)*np.exp(x)+(2*x-7)*np.exp(x)
    p0 = 1.2
    Nmax = 100
    tol = 1.e-10
    (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)

def newton(f,fp,p0,tol,Nmax):

    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        p[it+1] = p1
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
    p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]

driver()