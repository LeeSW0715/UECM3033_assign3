import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    # Edit here to implement your code
    # Let x = a point
    # Let w = weight
    [x, w] = np.polynomial.legendre.leggauss(n)
    
    # Using Gaussian Legendre formula here
    # (b-a) * Summation (weight * f ( (b-a)t(i) + b + a) )   
    #   /2                          (          /2        )
    # where b and a is the integration interval value
    #       t(i) is the x in this case which is legendere polynomial value

    # here I seperate the Gaussian Legendre into 3 parts to calculate
    p = 0
    p = (b - a) /2
    
    q = 0
    q = f(((b - a) / 2 * x) + ((b + a) / 2))
    
    r = 0
    r = sum (w * q)
    
    ans = p * r  
    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))
