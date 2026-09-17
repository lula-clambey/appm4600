import numpy as np
import matplotlib.pyplot as plt

#x*(1+((7-x**5)/x**2))**3
# x - ((x**5 - 7)/x**2)

    
def driver():

    f1 = lambda x: x*1+ ((x**5 - 7)/(5*x**4))
    f2 = lambda x: x - ((x**5 - 7)/12)
    Nmax = 100
    tol = 1e-10
    x = np.linspace(1.4,1.5,100) 
    x0 = 1.0

    [xstar,ier, count, xg] = fixedpt(f2,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f2(xstar):',f2(xstar))
    print('Error message reads:',ier)
    print('Iterations: ', count)

    plt.plot(x,f1(x))
    plt.plot(x,f2(x))
    plt.plot(x,x)
    iterations = xg[:count]
    plt.scatter(iterations, f2(iterations))
    plt.show()



# define routines
def fixedpt(f,x0,tol,Nmax):
    xg = np.zeros((Nmax,1))
    count = 0
    while (count <Nmax):
       x1 = f(x0)
       xg[count] = x1
       count = count +1
    
       if (abs(x1-x0)/abs(x1) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, count, xg]

       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, count, xg]
    

driver()
