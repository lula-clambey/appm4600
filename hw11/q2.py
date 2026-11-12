import numpy as np
from scipy.integrate import quad

"""def driver():
    f = lambda x: np.sin(x)
    a = 0
    b = np.pi
    n = 100
    h = (b-a)/n

    I_ex = quad(f,a,b)

    simpson = S(h,f,n,a,b)
    print('Simpson: ', simpson)

    romberg = 1/15*(S(h/2,f,n,a,b) - S(h,f,n,a,b))
    print('Romberg simpson: ', romberg)

def S(h,f,n,a,b):

    xnode = a+np.arange(0,n+1)*h
    I_simp = f(xnode[0])
    num_eval += 1
    nhalf = n/2
    
    for j in range(1,int(nhalf)):
        # even part
        I_simp = I_simp+2*f(xnode[2*j])
        # odd part
        I_simp = I_simp +4*f(xnode[2*j-1])
    
    I_simp= I_simp + f(xnode[n]) + 4*f(xnode[n-1])
    num_eval += 2
    I_simp = h/3*I_simp
    
    return I_simp

driver()"""


import matplotlib.pyplot as plt
import numpy as np
def driver():
    f = lambda x: np.sin(x)
    a = 0
    b = np.pi
    # exact integral
    I_ex = 2
    nrefine = 5
    # number of panels: 1, 2, 4, ..., 2^nrefine
    ntest = 2**np.arange(0,nrefine+1)
    Rom = rombergTrap(a,b,nrefine,f)

    # column j is only filled from row j down
    for j in range(0,nrefine+1):
        print('absolute error in column', j, '= ', abs(I_ex-Rom[j:,j]))
    err = abs(I_ex-np.diag(Rom))
    print('absolute error of best approximation at each order = ', err)
    plt.semilogy(ntest,err,'o-')
    plt.xlabel('n')
    plt.ylabel('absolute error')
    plt.show()

def rombergTrap(a,b,nrefine,f):
    # number of panels: 1, 2, 4, ..., 2^nrefine
    ntest = 2**np.arange(0,nrefine+1)

    nn = len(ntest)

    Rom = np.zeros((nn,nn))

    # first column: composite trapezoidal rule with n panels
    for j in range(0,nn):
        Rom[j,0] = CompSimp(a,b,ntest[j],f)

    # remaining columns: Richardson extrapolation
        for j in range(1,nn):
            for i in range(j,nn):
                Rom[i,j] = Rom[i,j-1] + (Rom[i,j-1]-Rom[i-1,j-1])/(4**(j+1)-1)
    
    return Rom


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