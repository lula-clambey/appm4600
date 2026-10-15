"""
This script provides you the opprotunity to insert your own line evaluator.
You will practice some python skills while getting a better understanding of
how splines work.
NOTE: this code will not compile until you add the line evaluator in the
appropriate location.
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv

def driver():
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval = np.linspace(a,b,Neval)
    ''' number of intervals'''
    Nint = 10
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
    plt.plot(xeval,fex,'ro-',label='exact function')
    plt.plot(xeval,yeval,'bs--',label='natural spline')
    plt.legend
    plt.show()
    err = abs(yeval-fex)
    plt.figure()
    plt.semilogy(xeval,err,'ro--',label='absolute error')
    plt.legend()
    plt.show()

def eval_lin_spline(xeval,Neval,a,b,f,Nint):
    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval)

    count = 0

    for jint in range(Nint):
        """
        find indices of xeval in interval (xint(jint),xint(jint+1))
        let ind denote the indices in the intervals
        let n denote the length of ind
        """

        '''temporarily store your info for creating a line in the interval of
        interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)

        for kk in range(10):
            '''use your line evaluator to evaluate the lines at each of the points
            in the interval'''
            '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with
            the points (a1,fa1) and (b1,fb1)'''
            yeval[count] = linebetween(a1,fa1,b1,fb1,xeval[count])
            count = count + 1

    return yeval

def linebetween(x0,fx0,x1,fx1,alpha):
    y = fx0 + ((fx1-fx0)/(x1-x0))*(alpha - x0)
    return y          

if __name__ == '__main__':
# run the drivers only if this is called from the command line
    driver()