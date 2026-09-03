import numpy as np
import matplotlib.pyplot as plt

def f(x,d):
    return np.cos(x+d)-np.cos(x)

def F(x,d):
    return -2*np.sin((2*x+d)/2)*np.sin(d/2)

d = 10**(np.linspace(0,-16,16))
x1 = np.pi
x2 = 10**6

plt.plot(d, abs(F(x1,d)-f(x1,d)), label = 'x=pi')
plt.plot(d, abs(F(x2,d)-f(x2,d)), label = 'x=10^6')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()