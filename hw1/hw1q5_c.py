import numpy as np
import matplotlib.pyplot as plt

#c = lambda x: np.cos(x)
#c1 = lambda x: -np.sin(x)
#c2 = lambda x: -np.cos(x)

d = 10**(np.linspace(-16,0,16))
x1 = np.pi
x2 = 10**6

def fc(x,d):
    return -d*np.sin(x) - ((d**2)/2)*np.cos(x)

def fb(x,d):
    return -2*np.sin((2*x+d)/2)*np.sin(d/2)

def c(x,d):
    return np.cos(x+d)-np.cos(x)

plt.plot(d, abs(fc(x1,d) - c(x1,d)), label = 'Part c')
plt.plot(d, abs(fb(x1,d) - c(x1,d)), label = 'Part b')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

plt.plot(d, abs(fc(x2,d) - c(x2,d)), label = 'Part c')
plt.plot(d, abs(fb(x2,d) - c(x2,d)), label = 'Part b')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()