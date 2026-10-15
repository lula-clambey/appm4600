import numpy as np
import matplotlib.pyplot as plt

def driver():
    N = 15
    f = lambda x: 1/(1+(10*x)**2)
    x = np.linspace(-.1,.1,1001)

    h = 2/(N-1)
    xi = np.zeros(N)
    for i in range(1,N+1):
        xi[i-1] = -1 + (i-1)*h

    plt.plot(x, P(x,xi,f,N))
    plt.show()

def P(x,xi,f,N):
    sum = 0
    for j in range(N):
        sum = sum + (wj(j,xi,N) / (x - xi[j]))*f(xi[j])
    P = phi_n(x,xi,N)*sum
    return P

def phi_n(x,xi,N):
    phi_n = 1.0
    for i in range(N):
        phi_n = phi_n*(x-xi[i])
    return phi_n

def wj(j,xi,N):
    dwj = 1.0
    for i in range(N):
        if i == j:
            continue
        dwj = dwj*(xi[j]-xi[i])
    return 1/dwj

driver()