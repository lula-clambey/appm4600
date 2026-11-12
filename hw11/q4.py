from scipy.special import gamma
from scipy.special import factorial
import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.integrate import quad

def driver():

    n = 100
    a = 0
    b = 100 #integral upper bound

    x_test = np.array([2,4,6,8,10])
    I_ex = gamma(x_test)
    I_trap, n_trap = CompTrap(a,b,n,x_test)

    #print('Exact: ', I_ex)
    #print('Trapezoid: ', I_trap)
    print('Trap Errors: ', abs(I_ex-I_trap))
    print('Trap eval: ', n_trap)

    I_quad = np.zeros((5))
    n_quad = np.zeros((5))
    for i in range(1,6):
        x = 2*i
        F = lambda t: t**(x-1)*np.exp(-t)
        I,err,info = quad(F,a,b, full_output=True)
        n_quad[i-1] = info['neval']
        I_quad[i-1] = I

    print('Quad error: ', abs(I_ex-I_quad))
    print('Quad eval: ', n_quad)

    #x = 10
    #I_ex = gamma(x)

    #t_nodes, w = laggauss(n)
    
    #I_lag = np.sum(w * (t_nodes ** (x-1)))
    
    #print('Gauss-Laguerre:     ', I_lag)
    #print('Error:    ', abs(I_ex - I_lag))


def f(x,t):
    return t**(x-1)*np.exp(-t)

def CompTrap(a,b,n,x):
    h = (b-a)/n
    num_eval = 0
    tnode = a+np.arange(0,n+1)*h
    I_trap = h*f(x,tnode[0])*1/2
    num_eval += 1

    for j in range(1,n):
        I_trap = I_trap+h*f(x,tnode[j])
        num_eval += 1

    I_trap= I_trap + 1/2*h*f(x,tnode[n])
    num_eval += 1

    return I_trap,num_eval

driver()