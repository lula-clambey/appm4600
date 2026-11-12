import numpy as np

def CompSimp(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    f0 = 0
    I_simp = f0 #f(xnode[0])
    nhalf = n/2

    for j in range(1,int(nhalf)):
        # even part
        I_simp = I_simp+2*f(xnode[2*j])
        # odd part
        I_simp = I_simp +4*f(xnode[2*j-1])

    I_simp= I_simp + f(xnode[n]) + 4*f(xnode[n-1])
    I_simp = h/3*I_simp

    return I_simp


a = 0
b = 1
n = 4
f = lambda x: x*np.cos(1/x)
I = CompSimp(a,b,n,f)
print(I)