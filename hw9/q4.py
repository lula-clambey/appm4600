import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x)
T = lambda x: x - x**3/6 + x**5/120
pa = lambda x: (x - (7/60)*x**3)/(1 + (1/20)*x**2)
pb = lambda x: (x - (7/60)*x**3)/(1 + (1/20)*x**2)
pc = lambda x: (x)/(1 + (1/6)*x**2 + (7/360)*x**4)

x = np.linspace(0,5,500)

plt.plot(x,f(x),'r', label = 'sin(x)')
plt.plot(x,T(x), 'b', label = 'taylor')
plt.plot(x,pc(x), 'g', label = 'pade')
plt.legend()
plt.show()

plt.plot(x,abs(f(x)-T(x)), 'b', label = 'taylor error')
plt.plot(x,abs(f(x)-pc(x)), 'g', label = 'pade error')
plt.legend()
plt.show()


