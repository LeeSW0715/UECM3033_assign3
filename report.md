UECM3033 Assignment #3 Report
========================================================

- Prepared by: Lee Soon Wah
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/LeeSW0715/UECM3033_assign3](https://github.com/LeeSW0715/UECM3033_assign3)


Explain how you implement your `task1.py` here.

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

Dealing with Gauss-Legendre quadrature, the important thing is need to have this code ‘[x, w] = np.polynomial.legendre.leggauss(n)’ at line 12 in code. This code will help to perform value x and w, x is the Legendre polynomial value t(i) and w is the weighting factor. By the way, code ‘def gausslegendre(f, a, b, n=20)’± at line 7 in code, is used to initialize the value of n with 20 terms in a given function and given value of integrate interval a and b. The value of n will brings to the line 12 codes which mention above to let the computer knows the number of terms  and perform the value of x and w to do the Gauss-Legendre quadrature. After some working steps then the Gauss Legendre answer will calculated and named as ‘ans’at line 31.

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

Define initially the value of n=20, then the value of weights and nodes will get by with code ‘np.polynomial.legendre.leggauss’.

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.

odeint is used to integrate a system of ordinary differential equations (ODE) with the initial value problem for stiff or non-stiff systems of first order ODE.
In this task, first define a name as Equation store variable y, t, a, and b
Where y is the value which gives to y0 and y1 
      t is the time in years between 0 and 5
      a and b is part of the equation which have values itself

Then the variable diff_equ will save the two different equation of Predator-prey into matrix form. After the Equation have value of all variables, then it will calculate the answer for diff_equ, the diff_equ will continue for plot two different graph. Using code ‘ans = odeint(Equation , y0 , time , args=(a,b))’ at line 25, clearly show that the function odeint needs the values from Equation, y0, time, and extra arguments which is a and b use to go through the ODE function. The same value of y0 will plot into two different condition, which is graphs of y(0) and y(1) against Time(Years), t ,and graph of y(1) against y(0). Lastly change the y0 with y1 at code line 54 then go through the same process of graph plotting.

Put your graphs here and explain.

Figure 1:














Figure 2:




Note : y0(t) = prey
	 y1(t) = predator
Based on the Graph 1 and 3 in Figure 1 and 2 respectively, it clearly observe that within 0 to 5 years, the number of prey will increase slowly but predator will decrease gradually. 
On the other hand, based on the Graph 2 and 3 in Figure 1 and 2 respectively, it shows when number of prey increase, the number of predator will decrease. it can conclude that there is an inverse relationship between prey and predator.
Besides, the value of y0(0) changes does not effect much on the graph, just changed the initial point of plotting on y-axis.

Is the system of ODE sensitive to initial condition? Explain.

The system of ODE is not much sensitive in initial condition, but it is need to depend on the changes of initial value. For this task, the changes of y0 = | 0.1 - 0.11 | = 0.01, there is not much big difference. If change the initial value to 100, y0 = | 0.1 - 100 | = 99.9, then the starting point will at very above at y1 = 100 at y0 = 0 on graph.

-----------------------------------

<sup>last modified: 2016 / April / 17</sup>


