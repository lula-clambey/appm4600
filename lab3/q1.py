import numpy as np

def driver():

    g = lambda x: (10/(x+4))**0.5

    Nmax = 100
    tol = 1e-10
    xg = np.zeros((Nmax,1))

#test g
    p0 = 1.5
    [xstar,ier,xg,count] = fixedpt(g, p0,tol,Nmax,xg)

    print('the approximate fixed point is:',xstar)
    print('g(xstar):',g(xstar))
    print('Error message reads:',ier)
    print('count: ', count)

    print('xg: ')
    for i in range(Nmax): 
        if xg[i,0] == 0:
            break
        print(xg[i,0])

    p = 1.3652300134140976
    p1 = xg[count-2]
    p2 = xg[count-3]
    p3 = xg[count-1]
    order = np.log(abs((p3-p)/(p1-p)))/np.log(abs((p1-p)/(p2-p)))
    print('order: ', order)

    avector = aitkins(xg, count)
    print('Aitkens vector: ')
    for j in range(count-2): 
        print(avector[j] , ", ")


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

def aitkins(xg,count):
    avector = np.zeros((count,1))
    for i in range(count-2):
        avector[i] = xg[i] - (xg[i+1] - xg[i])**2/(xg[i+2]-2*xg[i+1]+xg[i])
    return(avector)

    
driver()