import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    f = lambda x: np.e**x*np.cos(x)
    a = 0
    b = np.pi
    # exact integral
    I_ex = -12.070346316389632

    # N =100
    # ntest = np.arrange(0,N,step=2)
    # errorT = np.zeros(len(ntest))
    # errorS = np.zeros(len(ntest))
    # for j in range(0,len(ntest)):
    # n = ntest[j]
    # for simpson's n must be even.
    # n+1 = number of pts.

    n = 100
    err_trap = np.zeros(10)
    err_simp = np.zeros(10)
    h = np.zeros(10)
    for i in range(10): 
        I_trap = CompTrap(a,b,n,f)
        #print('I_trap= ', I_trap)
        err_trap[i] = abs((I_ex-I_trap)/I_ex)
        #print('absolute error = ', err)
        I_simp = CompSimp(a,b,n,f)
        #print('I_simp= ', I_simp)
        err_simp[i] = abs((I_ex-I_simp)/I_ex)
        #print('absolute error = ', err)
        h[i] = (b-a)/n
        n = n*2

    print('Trap: ',err_trap)
    print('Simp: ',err_simp)

    plt.plot(h,err_trap, label = 'Trap')
    plt.plot(h,err_simp, label = 'Simp')
    plt.loglog()
    plt.legend()
    plt.show()

def CompTrap(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    I_trap = h*f(xnode[0])*1/2

    for j in range(1,n):
        I_trap = I_trap+h*f(xnode[j])

    I_trap= I_trap + 1/2*h*f(xnode[n])

    return I_trap

def CompSimp(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    I_simp = f(xnode[0])
    nhalf = n/2

    for j in range(1,int(nhalf)):
        # even part
        I_simp = I_simp+2*f(xnode[2*j])
        # odd part
        I_simp = I_simp +4*f(xnode[2*j-1])

    I_simp= I_simp + f(xnode[n]) + 4*f(xnode[n-1])
    I_simp = h/3*I_simp

    return I_simp

driver()