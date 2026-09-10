import numpy as np


def driver():
# test functions
    f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....
    f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09...
    g = lambda x: (10/(x+4))**0.5

    Nmax = 100
    tol = 1e-10
    xg = np.zeros((Nmax,1))

# test f1 

    #x0 = 0.0
    #[xstar,ier,xg] = fixedpt(f1,x0,tol,Nmax,xg)

    #print('the approximate fixed point is:',xstar)
    #print('f1(xstar):',f1(xstar))
    #print('Error message reads:',ier)

    #for i in range(Nmax): 
    #    if xg[i,0] == 0:
    #        break
    #    print(xg[i,0], end=', ')


#test f2 
    #x0 = 0.0
    #[xstar,ier,xg] = fixedpt(f2,x0,tol,Nmax,xg)
    #print('the approximate fixed point is:',xstar)
    #print('f2(xstar):',f2(xstar))
    #print('Error message reads:',ier)

    #for i in range(Nmax): 
    #    if xg[i,0] == 0:
    #        break
    #    print(xg[i,0], end=', ')

#test g
    p0 = 1.5
    [xstar,ier,xg,count] = fixedpt(g, p0,tol,Nmax,xg)

    print('the approximate fixed point is:',xstar)
    print('g(xstar):',g(xstar))
    print('Error message reads:',ier)
    print('count: ', count)

    for i in range(Nmax): 
        if xg[i,0] == 0:
            break
        print(xg[i,0], end=', ')

    p = 1.3652300134140976
    p1 = xg[count-2]
    p2 = xg[count-3]
    p3 = xg[count-1]
    order = np.log(abs((p3-p)/(p1-p)))/np.log(abs((p1-p)/(p2-p)))
    print('order: ', order)


# define routines
def fixedpt(f,x0,tol,Nmax,xg):
    '''x0 = initial guess'''
    '''Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
        x1 = f(x0)
        xg[count,0] = x1
        count = count+1
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar,ier,xg,count]
        x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, xg, count]

    
driver()