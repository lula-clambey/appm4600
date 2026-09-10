import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x - 4*np.sin(2*x) - 4

x = np.linspace(-20, 20, 4000)

plt.plot(x,f(x))
plt.axhline(0, color = 'black')
plt.axvline(0, color = 'black')
plt.show()