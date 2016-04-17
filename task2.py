import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 1.0
b = 0.2

# Perform an ODE into differential equation which given
def Equation(y , t , a , b):
    # let y0 and y1 be y value
    y0, y1 = y
    # Seperate the given function y0' = p and y1' = q
    p = a * (y0 - (y0 * y1))
    q = b * (-y1 + (y0 * y1))
    # Let diff_equ be one matrix to store the value of p and q 
    diff_equ = [p , q]
    return diff_equ
  
# Let time = time in 0 to 5 years
time = np.linspace(0, 5, 10)    

# Let y0 be a matrix store value y0(0) = 0.1 and y1(0) = 1.0 as given
y0  =  [0.1,1.0]
ans = odeint(Equation , y0 , time , args=(a,b))
    
# Plot for y0 and y1 against time
plt.figure()
plt.subplot(121)

plt.plot(time, ans[:, 0], 'r', label='y0(t)')
plt.plot(time, ans[:, 1], 'b', label='y1(t)')
plt.legend(loc = 'best')
plt.grid(True)
plt.ylabel('y(t)')
plt.xlabel('Time (years) , t')
plt.title(' Graph 1 : y0 and y1 against Time,t')
plt.grid()
plt.show()

# Plot for y1 against y0
plt.subplot(122)
plt.plot(ans[:,0], ans[:,1], 'g')
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('y0')
plt.ylabel('y1')
plt.title('Graph 2 : y0 against y1')
plt.grid(True)
plt.legend(loc = 'best')
plt.grid()
plt.show()

# Let y1 be a matrix store value y0(0) = 0.11 and y1(0) = 1.0 as given
y1  =  [0.11,1.0]
ans = odeint(Equation , y1 , time , args=(a,b))
# Plot for y0 and y1 against time
plt.figure()
plt.subplot(121)
plt.plot(time, ans[:, 0], 'r', label='y0(t)')
plt.plot(time, ans[:, 1], 'b', label='y1(t)')
plt.legend(loc = 'best')
plt.grid(True)
plt.ylabel('y(t)')
plt.xlabel('Time (years) , t')
plt.title('Graph 3 : new value of y0 and y1 against Time,t')
plt.grid()
plt.show()

# Plot for y1 against y0
plt.subplot(122)
plt.plot(ans[:,0], ans[:,1] ,'g')
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('y0')
plt.ylabel('y1')
plt.title('Graph 4 : new value of y0 against y1')
plt.grid(True)
plt.legend(loc = 'best')
plt.grid()
plt.show()