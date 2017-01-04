#File ejemploag.py
#Example of GA
#Dr. Jorge Luis Rosas Trigueros
#Last change: 21sep15

from Tkinter import *
import math
import random
#Chromosomes are 4 bits long
#Como no hay una cadena que sea extrictamente cero nunca llega a cero
#REGISTRAR EL VALOR con 4 bits
L_chromosome=16
N_chains= 2**L_chromosome #poblacion
#Lower and upper limits of search space

#espacio de busqueda
a=-5.12
b=5.12
crossover_point=L_chromosome/2#punto de cruce

#cadena con dos variables arreglo mitad x y mitad y
def random_chromosome():#generamos un cromosoma
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.1:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome


#Number of chromosomes
N_chromosomes=10
#probability of mutation
#prob_m=0.1
#prob_m=0.25
#prob_m=0.5
prob_m=0.75


F0=[]#poblacion original, antes de ser mutada
fitness_values=[]#valores de aptitud de cada inidividuo

#generamos los individuos de la poblacion original
for i in range(0,N_chromosomes): #array de cromosomas
    F0.append(random_chromosome())
    fitness_values.append(0)#llenamos de ceros 


#binary codification-->FENOTIPO
def decode_chromosome(chromosome):
    global L_chromosome,N_chains,a,b
    value=0
    value2=0
    for p in range(0,L_chromosome/2):
        value+=(2**p)*chromosome[-1-p]

    for p in range(L_chromosome/2, L_chromosome):
        value2+=(2**p)*chromosome[-1-p]

    return (a+(b-a)*float(value)/(N_chains-1),a+(b-a)*float(value2)/(N_chains-1))


#funcion de aptitud, es una parabola, genera muchos max y min locales
#modificar enviar dos parametros f(x,y)
def f(x,y):
    #return 0.05*x*x-4*math.cos(x)
    return ((20.0) + ((x**2)- (10.0*(math.cos((2.0*math.pi)*x)))) + ((y**2) - (10.0*(math.cos((2.0*math.pi)* y)))))

#evaluamos su funcion de aptitud
def evaluate_chromosomes():
    global F0
    for p in range(N_chromosomes):
        (v,v1)=decode_chromosome(F0[p])
        fitness_values[p]=f(v,v1)
        
#funcion de comparacion con sort, definimos como se
#van a comparar , se comparan las funciones de los
#cromosomas
def compare_chromosomes(chromosome1,chromosome2):
    (vx1,vy1)=decode_chromosome(chromosome1)
    (vx2,vy2)=decode_chromosome(chromosome2)
    fvc1=f(vx1,vy1)
    fvc2=f(vx2,vy2)
    if fvc1 > fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1


suma=float(N_chromosomes*(N_chromosomes+1))/2.

Lwheel=N_chromosomes*10

#El mas alto va a tener mas boletos en la ruleta
#y el menos menos boletos
def create_wheel():
    global F0,fitness_values

    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        acc+=maxv-fitness_values[p]
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel
##    print fraction
    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2
##    print fraction

    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
        
F1=F0[:]

#Evaluamos, ordenamos la poblacion inicial f0
#CON EL ELITISMO GARANTIZAMOS de que llegue al optimo
#Se genera la ruleta y se sacan dos individuos que
#van a ser los progenitores
#Luego damos un valor alto de probabilidad de mutacion
#se le hace un XOR para mutar y se agregan a la poblacion de 
#descendencia
n_generation=0
def nextgeneration():
    global n_generation
    n_generation+=1
    print n_generation
    
    F0.sort(cmp=compare_chromosomes)
    print "Best solution so far:"
    (x,y)=decode_chromosome(F0[0])
    print "f(",decode_chromosome(F0[0]),")= ", f(x,y)
                                                                    
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    
    for i in range(0,(N_chromosomes-2)/2):
        roulette=create_wheel()
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    #The generation replaces the old one
    F0[:]=F1[:]

F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()

for i in range(1,100):

	nextgeneration()
