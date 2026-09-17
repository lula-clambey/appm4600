import numpy as np

#x*(1+((7-x**5)/x**2))**3
# x - ((x**5 - 7)/x**2)

    
def driver():


     f2 = lambda x: x - ((x**5 - 7)/12)
     Nmax = 100
     tol = 1e-10

    
     x0 = 1.0
     [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):
    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)

       if (abs(x1-x0)/abs(x1) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]

       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()
