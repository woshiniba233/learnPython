from sympy import *
x=Symbol('x')
y=Symbol('y')
print solve([y+x-1,3*x+2*y-5],[x,y])

while 1:
    print solve(input("input function like \'x**2 + 2*x + 1\' : "))
