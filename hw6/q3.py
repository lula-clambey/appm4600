import numpy as np
import math
from numpy.linalg import inv
from numpy.linalg import norm
def driver():
    Nmax = 100
    x0= np.array([0,1,1])
    tol = 1e-6

    [xstar,ier,its] = Newton(x0,tol,Nmax)
    print("the newton code found the solution ",xstar)
    print("the newton code number iterations ",its)
    print("ier is ", ier )

    [xstar,gval,its,ier] = SteepestDescent(x0,tol,Nmax)
    print("the steepest descent code found the solution ",xstar)
    print("steepest descent iterations: ",its)
    print("g evaluated at this point is ", gval)
    print("ier is ", ier )

    [xstar,gval,its,ier] = combo(x0,tol,Nmax)
    print("the combo code found the solution ",xstar)
    print("combo iterations: ",its)
    print("g evaluated at this point is ", gval)
    print("ier is ", ier )



def evalF(x):
# vector valued function you are trying to find the root of
    F = np.zeros(3)
    F[0] = x[0] +math.cos(x[0]*x[1]*x[2])-1
    F[1] = (1-x[0])**(0.25) + x[1] +0.05*x[2]**2 -0.15*x[2]-1
    F[2] = -x[0]**2-0.1*x[1]**2 +0.01*x[1]+x[2] -1
    return F

def evalJ(x):
# Jacobian of the vector valued function you are trying to find the root of.
    J=np.array([[1.-x[1]*x[2]*math.sin(x[0]*x[1]*x[2]),-x[0]*x[2]*math.sin(x[0]*x[1]*x[2]
    ),-x[1]*x[0]*math.sin(x[0]*x[1]*x[2])],
    [-0.25*(1-x[0])**(-0.75),1,0.1*x[2]-0.15],
    [-2*x[0],-0.2*x[1]+0.01,1]])
    return J

def evalg(x):
    # The least squares function you are minimizing
    F = evalF(x)
    g = F[0]**2 + F[1]**2 + F[2]**2
    return g

def eval_gradg(x):
    # Grad g
    F = evalF(x)
    J = evalJ(x)
    gradg = np.transpose(J).dot(F)
    return gradg


def Newton(x0,tol,Nmax):
    for its in range(Nmax):
        J = evalJ(x0)
        Jinv = inv(J)
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier, its]
        x0 = x1
    xstar = x1
    ier = 1
    return[xstar,ier,its]

### steepest descent code
def SteepestDescent(x,tol,Nmax):
    for its in range(Nmax):
        g1 = evalg(x)
        z = eval_gradg(x)
        z0 = norm(z)
        if z0 == 0:
            print("zero gradient")
        z = z/z0
        alpha1 = 0
        alpha3 = 1
        dif_vec = x - alpha3*z
        g3 = evalg(dif_vec)

        while g3>=g1:
            alpha3 = alpha3/2
            dif_vec = x - alpha3*z
            g3 = evalg(dif_vec)

        if alpha3<tol:
            print("no likely improvement")
            ier = 0
            return [x,g1,its,ier]
        
        alpha2 = alpha3/2
        dif_vec = x - alpha2*z
        g2 = evalg(dif_vec)

        h1 = (g2 - g1)/alpha2
        h2 = (g3-g2)/(alpha3-alpha2)
        h3 = (h2-h1)/alpha3

        alpha0 = 0.5*(alpha2 - h1/h3)
        dif_vec = x - alpha0*z
        g0 = evalg(dif_vec)

        if g0<=g3:
            alpha = alpha0
            gval = g0
        else:
            alpha = alpha3
            gval =g3

        x = x - alpha*z

        if abs(gval - g1)<tol:
            ier = 0
            return [x,gval,its,ier]
        
    print('max iterations exceeded')
    ier = 1
    return [x,g1,its,ier]

def combo(x,tol,Nmax):
    for its in range(Nmax):
        g1 = evalg(x)
        z = eval_gradg(x)
        z0 = norm(z)
        if z0 == 0:
            print("zero gradient")
        z = z/z0
        alpha1 = 0
        alpha3 = 1
        dif_vec = x - alpha3*z
        g3 = evalg(dif_vec)

        while g3>=g1:
            alpha3 = alpha3/2
            dif_vec = x - alpha3*z
            g3 = evalg(dif_vec)

        if alpha3<tol:
            print("no likely improvement")
            ier = 0
            return [x,g1,its,ier]
        
        alpha2 = alpha3/2
        dif_vec = x - alpha2*z
        g2 = evalg(dif_vec)

        h1 = (g2 - g1)/alpha2
        h2 = (g3-g2)/(alpha3-alpha2)
        h3 = (h2-h1)/alpha3

        alpha0 = 0.5*(alpha2 - h1/h3)
        dif_vec = x - alpha0*z
        g0 = evalg(dif_vec)

        if g0<=g3:
            alpha = alpha0
            gval = g0
        else:
            alpha = alpha3
            gval =g3

        x = x - alpha*z

        if abs(gval - g1)<5e-2:
            for its2 in range(Nmax):
                J = evalJ(x)
                Jinv = inv(J)
                F = evalF(x)
                x1 = x - Jinv.dot(F)
                if (norm(x1-x) < tol):
                    xstar = x1
                    g1 = evalg(xstar)
                    ier =0
                    return[xstar, g1, its+its2, ier]
                x = x1          
            xstar = x1
            g1 = evalg(xstar)
            ier = 1
            return[xstar,g1,its+its2,ier]
            
    print('max iterations exceeded')
    ier = 1
    return [x,g1,its+its2,ier] 


if __name__ == '__main__':
# run the drivers only if this is called from the command line
    driver()