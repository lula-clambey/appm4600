import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
"""
xval = np.linspace(-5,5,1000)
f = lambda x: 1/(1+x**2)
fpp = lambda x: 8*x**2/(1+x**2)**3 - 2/(1+x**2)**2
fpppp = lambda x: (24*(5*x**4-10*x**2+1))/(1+x**2)**5

plt.plot(xval,f(xval), label = 'f')
plt.plot(xval,fpp(xval), label = 'f(2)')
plt.plot(xval,fpppp(xval), label = 'f(4)')
plt.legend()
plt.show()

print(fpppp(0))
"""

def driver():
    f = lambda x: 1/(1+x**2)
    a = -5
    b = 5
    I_ex, err, info = quad(f,a,b, epsabs=1e-4, full_output = True)
    n_ex = info['neval']
    n_trap = 1291
    n_simp = 108


    [I_trap,num_trap] = CompTrap(a,b,n_trap,f)
    print('Trap evalutation: ', num_trap)

    [I_simp,num_simp] = CompSimp(a,b,n_simp,f)
    print('Simp evaluations: ', num_simp)

    print('Exact evaluations: ', n_ex)
    print('Exact error: ', err)


def CompTrap(a,b,n,f):
    h = (b-a)/n
    num_eval = 0
    xnode = a+np.arange(0,n+1)*h
    I_trap = h*f(xnode[0])*1/2
    num_eval += 1

    for j in range(1,n):
        I_trap = I_trap+h*f(xnode[j])
        num_eval += 1

    I_trap= I_trap + 1/2*h*f(xnode[n])
    num_eval += 1

    return I_trap, num_eval

def CompSimp(a,b,n,f):
    h = (b-a)/n
    num_eval = 0
    xnode = a+np.arange(0,n+1)*h
    I_simp = f(xnode[0])
    num_eval += 1
    nhalf = n/2

    for j in range(1,int(nhalf)):
        # even part
        I_simp = I_simp+2*f(xnode[2*j])
        num_eval += 1
        # odd part
        I_simp = I_simp +4*f(xnode[2*j-1])
        num_eval += 1

    I_simp= I_simp + f(xnode[n]) + 4*f(xnode[n-1])
    num_eval += 2
    I_simp = h/3*I_simp

    return I_simp, num_eval

driver()