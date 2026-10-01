import matplotlib.pyplot as plt

def driver():
    f = lambda x: x**6 - x - 1
    fp = lambda x: 6*x**5 -1
    x0 = 2
    x1 = 1
    tol = 1e-8
    Nmax = 100
    print('Newton: ')
    [n, nerr] = newton(f,fp, x0, tol, Nmax)
    print('Newton root: ', n)
    print('Newton error: ', nerr)
    print('Secant: ')
    [s, serr] = secant(f, x0, x1, tol, Nmax)
    print('Secant root: ', s)
    print('Secant error: ', serr)

    plt.xscale('log')
    plt.yscale('log')
    plt.show()


def newton(f,fp,p0,tol,Nmax):
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        print('Error ', it, ' : ', abs(p1 - 1.1347241384015194))
        plt.plot(abs(p0 - 1.1347241384015194), abs(p1-1.1347241384015194), 'ro')
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [pstar, info]
        p0 = p1

    pstar = p1
    info = 1
    return [pstar, info]

def secant(f, x0, x1, tol, Nmax):
    if abs(f(x1)-f(x0)) == 0:
        ier = 1
        pstar = x1
        return [pstar, ier]

    for it in range(Nmax):
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        print('Error ', it, ' : ', abs(x2-1.1347241384015194))
        plt.plot(abs(x1 - 1.1347241384015194), abs(x2-1.1347241384015194), 'bo')
        if abs(x2-x1) < tol:
            pstar = x2
            ier = 0
            return [pstar, ier]
        x0 = x1
        x1 = x2

    pstar = x2
    ier = 1
    return [pstar, ier]

driver()