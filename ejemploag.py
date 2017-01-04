from Tkinter import *
import math
import random

#Chromosomes are 4 bits long
L_chromosome=4
#poblacion
N_chains= 2**L_chromosome 
#espacio de busqueda
a=-20
b=20
#punto de cruce
crossover_point=L_chromosome/2
#Number of chromosomes
N_chromosomes=10
#probability of mutation
#prob_m=0.1
prob_m=0.25
#prob_m=0.75
#prob_m=0.5
F0=[]#poblacion original, antes de ser mutada
fitness_values=[]#valores de aptitud de cada inidividuo

#generamos un cromosoma
def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.1:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome

#inicializacion de la poblacion de cromosomas junto con su valor de aptitud
for i in range(0,N_chromosomes): 
    F0.append(random_chromosome())
    fitness_values.append(0) 


#binary decodie FENOTIPO
def decode_chromosome(chromosome):
    global L_chromosome,N_chains,a,b
    value=0
    for p in range(L_chromosome):
        value+=(2**p)*chromosome[-1-p]

    return a+(b-a)*float(value)/(N_chains-1)


#funcion de aptitud, es una parabola, genera muchos max y min locales
#modificar enviar dos parametros f(x,y)
def f(x):
    #return 0.05*x*x-4*math.cos(x)
    d= N_chromosomes;
    a=20
    b=0.2
    c=2*math.pi

    sum1=0
    sum2=0

    for ii in range(1,d): 
    	xi= F0[ii]
    	sum1= sum1 + (xi*xi)
    	sum2= sum2 + math.cos(c*xi)

    term1= -a*math.exp(-b*math.sqrt(sum1/d))
    term2=-math.exp(sum2/d)

    return term1 + term2 + a + exp(1)

#evaluamos su funcion de aptitud
def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        v=decode_chromosome(F0[p])#decodificamos cada cromosoma
        fitness_values[p]=f(v)#ese valor lo evaluamos en la funcion de fitness y regresa una poderacion
        
#funcion de comparacion con sort, definimos como se
#van a comparar , se comparan las funciones de los
#cromosomas
def compare_chromosomes(chromosome1,chromosome2):
    vc1=decode_chromosome(chromosome1)
    vc2=decode_chromosome(chromosome2)
    fvc1=f(vc1)
    fvc2=f(vc2)
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
    w.delete(ALL)
    F0.sort(cmp=compare_chromosomes)
    print "Best solution so far:"
    print "f(",decode_chromosome(F0[0]),")= ", f(decode_chromosome(F0[0]))
                                                                    
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

    graph_f()
    graph_population(F0,w,s,s,xo,yo,'SpringGreen2')
    graph_population(F1,w,s,s*0.5,xo,yo,'yellow')
    #The generation replaces the old one
    F0[:]=F1[:]


#visualization
master = Tk()

xmax=400
ymax=400

xo=200
yo=200

s=10

w = Canvas(master, width=xmax, height=ymax)
w.pack()
w.config(background='DeepSkyBlue3')

            
button1 = Button(master, text="Next Generation", command=nextgeneration)
button1.pack()

N=100


def graph_f():
    xini=-20.
    xfin=20.

    dx=(xfin-xini)/N

    xold=xini
    yold=f(xold)
    for i in range(1,N):
        xnew=xini+i*dx
        ynew=f(xnew)
        w.create_line(xo+xold*s,yo-yold*s,xo+xnew*s,yo-ynew*s,fill='snow')
        xold=xnew
        yold=ynew

def graph_population(F,mycanvas,escalax,escalay,xcentro,ycentro,color):
    for chromosome in F:
        x=decode_chromosome(chromosome)
        mycanvas.create_line(xcentro+x*escalax,ycentro-10*escalay,xcentro+x*escalax, ycentro+10*escalay,fill=color)


graph_f()
graph_population(F0,w,s,s,xo,yo,'orange')
F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()

mainloop()
