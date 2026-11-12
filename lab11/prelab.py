import numpy as np



def evalTrap(a,b,f,N):
    h = (b-a)/N
    xnode = a+np.arange(0,n+1)*h
    I_trap = h*f(xnode[0])*1/2
    
    for j in range(1,n):
        I_trap = I_trap+h*f(xnode[j])
    
    I_trap= I_trap + 1/2*h*f(xnode[n])
    
    return I_trap

def evalSimp(a,b,f,N):
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