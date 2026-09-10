import numpy as np

x = 9.999999995000000*10**-10

def driver(x):
    y = np.e**x
    return y-1

def f(x):
   return x + x**2/2 

print(driver(x))
print(f(x))