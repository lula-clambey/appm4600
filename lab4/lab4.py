import numpy as np

def driver():
 
    f = lambda x: np.e**(x**2 + 7*x -30) - 1
    fp = lambda x: (2*x + 7) * np.e**(x**2 + 7*x -30)
    fpp = lambda x: (2*x + 7)**2 * np.e**(x**2 + 7*x -30)
    a = 2
    b = 4.5

    tol = 1e-8
    Nmax = 100

    [bisec_only, count, ier] = bisection(f, a, b, tol)
    print('Bisection only root:', bisec_only)
    print('Bisection only count: ', count)
    print('Bisection only error: ', ier)

    p0 = 4.5
    [newton_only, count, ier] = newton(f, fp, p0, tol, Nmax)
    print('Newton only root: ', newton_only)
    print('Newton only count: ', count)
    print('Newton only error: ', ier)

    [both,count,ier] = bisection_netwon(f,fp, fpp, a,b,tol, Nmax)
    print('Combo root: ',both)
    print('Combo count: ', count)
    print('Combo error:',ier)
    #print('f(astar) =', f(astar)) 

def bisection(f,a,b,tol):
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier]
    if (fa == 0):
        astar = a
        ier =0
        return [astar, ier]
    if (fb ==0):
        astar = b
        ier = 0
        return [astar, ier]
    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
        fd = f(d)
        if (fd ==0):
            astar = d
            ier = 0
            return [astar, ier]
        if (fa*fd<0):
            b = d
        else: 
            a = d
            fa = fd
        d = 0.5*(a+b)
        count = count +1
        
    astar = d
    ier = 0
    #print('count = ', count)
    return [astar, count, ier]

def newton(f,fp,p0,tol,Nmax):

    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
    if (abs(p1-p0) < tol):
        pstar = p1
        info = 0
        return [pstar,it, info]
    p0 = p1
    pstar = p1
    info = 1
    return [pstar,it, info]


def bisection_netwon(f, fp, fpp, a,b,tol, Nmax):
    count = 0
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, count, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, count, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, count, ier]

    d = 0.5*(a+b)

    while (abs((f(d)*fpp(d))/(fp(d))**2) >= 1):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, count, ier]
         
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    #print('count = ', count)

    p0 = astar
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        if (abs(p1-p0) < tol):
            pstar = p1
            ier = 0
            return [pstar, count+it, ier]
        p0 = p1
        pstar = p1
        ier = 1

    count = count + it
    return [pstar, count, ier]

     
driver()               


