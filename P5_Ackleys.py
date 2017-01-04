
from Tkinter import *
from numpy import *
#import random

lower_limit=-20
upper_limit=20
n_particles=10
n_dimensions=2

# Initialize the particle positions and their velocities
X = lower_limit + (upper_limit - lower_limit) * random.rand(n_particles, n_dimensions) 
#print "X:",X
assert X.shape == (n_particles, n_dimensions)

V = zeros(X.shape)
assert V.shape == (n_particles,n_dimensions)
#print "V:",V

X_lbest=1*X
assert X_lbest.shape == (n_particles, n_dimensions)
#print "X_lbest",X_lbest

X_gbest= 1*X_lbest[0]
X_gbest.shape == ( 1,n_dimensions)
#print "X_gbest",X_gbest

#evaluamos por parejas
def f(x,y):
    #return 0.05*x*x-4*math.cos(x)
    return ((20.0) + ((x**2)- (10.0*(math.cos((2.0*math.pi)*x)))) + ((y**2) - (10.0*(math.cos((2.0*math.pi)* y)))))

for I in range(0, n_particles):
    if f(X_lbest[I][0],X_lbest[I][1])<f(X_gbest[0],X_gbest[1]):
        X_gbest[0]=1*X_lbest[I][0]
        X_gbest[1]=1*X_lbest[I][1]

#print "X_gbest desp",X_gbest

def iteracion():
    global X,X_lbest,X_gbest,V

    weight=0.3
    C1=0.3
    C2=0.3
    print "Best particle in:",X_gbest[0],X_gbest[1]," gbest: ",f(X_gbest[0],X_gbest[1])
    # Update the particle velocity and position
    for I in range(0, n_particles):
        #for J in range(0, n_dimensions):
          #pick random numbers for rp and rg
        R1 = random.rand()#rp
        R2 = random.rand()#rg
          #updating velocity
        V[I][0] = (weight*V[I][0]+ C1*R1*(X_lbest[I][0] - X[I][0])+ C2*R2*(X_gbest[0] - X[I][0]))
        V[I][1] = (weight*V[I][1]+ C1*R1*(X_lbest[I][1] - X[I][1]) + C2*R2*(X_gbest[1] - X[I][1]))
          #updating best particle(solution)
        X[I][0] = X[I][0] + V[I][0]
        X[I][1] = X[I][1] + V[I][1]
        #updating lider and best position
        if f(X[I][0],X[I][1])<f(X_lbest[I][0],X_lbest[I][1]):
            X_lbest[I][0]=1*X[I][0]#Pid
            X_lbest[I][1]=1*X[I][1]#Pid
        if f(X_lbest[I][0],X_lbest[I][1])<f(X_gbest[0],X_gbest[1]):
            X_gbest[0]=1*X_lbest[I][0]#g
            X_gbest[1]=1*X_lbest[I][1]#g
          
for K in range(10):
    iteracion()