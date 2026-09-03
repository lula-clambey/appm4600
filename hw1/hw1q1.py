import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.920, 2.081, .001)

p1 = lambda x: x**9 - 18*x**8 + 144*x**7 - 672*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512
P1 = p1(x)
p2 = lambda x: (x-2)**9
P2 = p2(x)

plt.plot(x, P1)
plt.xlabel('x')
plt.ylabel('p coefficients')
plt.show()

plt.plot(x, P2)
plt.xlabel('x')
plt.ylabel('p expression')
plt.show()


