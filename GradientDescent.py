import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sympy as sym
from sympy import *


X = [1,2,3]
Y = [1,2,3]

w , b = symbols("w,b")
m = len(X)
J = 0

for i in range (0,len(X)):
     J = J + (0.5/m)* (w * X[i]+b - Y[i])**2
    
#J=(0.5/m)*((w * X[0]+b - Y[0])**2 +(w * X[1]+b - Y[1])**2 + (w * X[2]+b - Y[2])**2)

Jw = diff (J,w)
Jb = diff (J,b)

Jw = lambdify ([w,b],Jw)
Jb = lambdify ([w,b],Jb)

J = lambdify ([w,b],J)
alpha = 0.001
w=0.5
b=0.5
X3 = []
W= []
B=[]
for i in range (0,100000):
    
    X3.append(i)
    w1 = w - alpha * Jw(w,b)
    b1 = b - alpha * Jb(w,b)
    
    w = w1
    b = b1
    W.append(w)
    B.append(b)
    #print("w is...",w,"b is ...",b)

x2 = np.linspace(0,10,100)
y2 = w * x2 + b
print ( "b is: ",b )
print("w is: ",w)
cost=[]
for i in range (0,len(W)):
    cost.append (J(W[i],B[i]))

print("J is: ",J(w,b))


            

#plt.title ("Testing for convergence")
# plt.xlabel("iterations")
# plt.ylabel("Cost")
#plt.plot(X3,cost )
#plt.grid()
#plt.show()



#plt.title ("Gradient Descent")
# plt.xlabel("x")
# plt.ylabel("y")
#plt.plot(x2,y2)
#plt.scatter(X,Y)
#plt.grid()
#plt.show()




J_vals = []


x = np.linspace(-20,20,100)
y = np.linspace(-20,20,100)

A,B = np.meshgrid(x,y)
#print("A: ",A, "and B: ",B)
J_vals = J(A,B)

#for i in range (0,len(W)):
 #   J_vals.append( J(W[i],B[i]) )

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.plot_wireframe(A,B,J_vals,color='green')
ax.set_title('3D line plot adsadsdad')
plt.xlabel('w')
plt.ylabel('b')
plt.show()



