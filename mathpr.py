#sympy to calulate limit
from sympy import *
import math
#matplotlib to calculate graph
import matplotlib.pyplot as plt
 
n = symbols('n')
u = sin(1/n)/n
v=(1/(n**2))
f=u/v
print("\n")
print("u : {}".format(u))

print("v : {}".format(v))

print("u/v : {}".format(f))
print("\n")
# Use sympy.limit() method
limit_expr = limit(f, n, math.inf) 
     
print("Limit of the expression(u/v) n-->infinity = {}".format(limit_expr)) 
print("Limit is finite and non zero")
print("/n")
print("We know that by camparision test u and v have same property")
print("And by P- series test")
print("v={}".format(v))
p=2
print("p =",p) 
print("Clearly p is greater the 1")
print("Hence v is convergent therefore u is also convergent")

print("\n")
print("Convergence test by graph")
print("\n")

n=int(input("Enter the limit(n value):"))
sum=0
x=[]
y=[]
for i in range(1,n+1):
     sum+=sin(1/i)*(1/i)
     y+=[sum]
     x+=[i]
print("Sum =",sum)  
print("When n-->infinity the value of partial sum is fixed i.e ,1.4727282369560746 that is a finite value hence series is convergent")

plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("sum")
plt.show()

