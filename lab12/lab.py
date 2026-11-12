import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time

def driver():
    ''' create matrix for testing different ways of solving a square
    linear system'''

    """
    '''' N = size of system'''
    N = 100
    print('N: ', N)
    ''' Right hand side'''
    b = np.random.rand(N,1)

    A = np.random.rand(N,N)

    start = time.time()
    x_solve = scila.solve(A,b)
    end = time.time()
    elapsed = end-start
    print('solve time: ', elapsed)
    #print('solve x: ', x_solve)

    #test = np.matmul(A,x_solve)
    #r = la.norm(test-b)
    #print(r)

    start = time.time()
    LU, pivot = scila.lu_factor(A)
    t2 = time.time()
    x_lu = scila.lu_solve((LU, pivot), b)
    end = time.time()
    elapsed = end-start
    factor = t2-start
    solved = end-t2
    print('lu total time: ', elapsed)
    print('lu factorization: ', factor)
    print('lu solved: ', solved)
    #print('lu x: ', x_lu)
    """

    ''' Create an ill-conditioned rectangular matrix '''
    N = 10
    M = 5
    A = create_rect(N,M)
    b = np.random.rand(N,1)

    #normal
    Ap = A.T@A
    bp = A.T@b
    x_normal = la.solve(Ap,bp)

    #QR
    Q,R = la.qr(A)
    y = Q.T@b
    x_qr = la.solve(R,y)



def create_rect(N,M):
    ''' this subroutine creates an ill-conditioned rectangular matrix'''
    a = np.linspace(1,10,M)
    d = 10**(-a)
    D2 = np.zeros((N,M))
    for j in range(0,M):
        D2[j,j] = d[j]

    '''' create matrices needed to manufacture the low rank matrix'''
    A = np.random.rand(N,N)
    Q1, R = la.qr(A)
    test = np.matmul(Q1,R)
    A = np.random.rand(M,M)
    Q2,R = la.qr(A)
    test = np.matmul(Q2,R)
    B = np.matmul(Q1,D2)
    B = np.matmul(B,Q2)
    return B

if __name__ == '__main__':
# run the drivers only if this is called from the command line
    driver()