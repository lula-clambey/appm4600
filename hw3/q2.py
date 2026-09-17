import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

def f(x):
    return 35*erf(x/(2*(5184000*0.138*10**-6)**0.5)) - 15

xbar = 5
tol = 1e-13
x = np.linspace(0,xbar,500)
#plt.plot(x,f(x))
#plt.show()

#bisection
def bisection(tol, xbar):
    tol = tol
    a=0
    b=xbar
    d = 0.5*(a+b)
    xstar = a
    fa = f(a)
    
    while(abs(b-a) > tol):
        fd = f(d)

        if (fd == 0):
            xstar = d
            return xstar
        
        if (fa*fd < 0):
            b=d
        else:
            a = d
            fa = fd

        d = 0.5*(a+b)
        xstar = d
    return xstar


#newtons
def newton(tol):
    tol = tol
    Nmax = 100
    x0 = .6769

    fp = lambda x: (70/np.pi**0.5)*np.exp(-x**-2)

    for i in range(Nmax):
        x1 = x0 - f(x0)/fp(x0)
        if (abs(x1-x0) < tol):
            xstar = x1
            return xstar
        
        x0 = x1

    xstar = x1
    return xstar

print('Bisection root: ', bisection(tol, xbar))
print('Newton root: ', newton(tol))
