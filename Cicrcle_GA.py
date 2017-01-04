
from Tkinter import *
import math
import random


points=[(5,3),(5,7),(7,5)]
Nbits_h =8
Nbits_k=8
N_bits_r=8
L_chromosome = Nbits_h + Nbits_k + N_bits_r

prob_m=0.75      #probability of mutation
N_chromosomes=10 #Number of chromosomes

N_chains=2**L_chromosome
crossover_point=L_chromosome/2

F0=[]
fitness_values=[]
Lwheel=N_chromosomes*10


def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.5:
            chromosome.append(0)
        else:
            chromosome.append(1)
    return chromosome

for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)

def decode_float(lowerlimit, upperlimit, bits):
    L_bits = len(bits)
    N_chains = 2**L_bits
    value=0
    for p in range(L_bits):
        value+=(2**p)*bits[-1-p]
    return lowerlimit+(upperlimit-lowerlimit)*float(value)/(N_chains-1)

def decode_chromosome(chromosome):
   #Los puntos pueden oscilar de 0 a 10 para X y Y
   h=decode_float(0,10,chromosome[: Nbits_h])
   k=decode_float(0,10,chromosome[Nbits_h : Nbits_h + Nbits_k])
   #el radio como maximo puede ser 5, si no se pasaria del espacio de 10x10
   R=decode_float(0,5,chromosome[Nbits_h+Nbits_k :])
   return h,k,R;


def f(x):
    global points
    h,k,R=x
    error=0
#se usa la formula (x-h)(x-h) + (y-k)(-k)=r*r para obtener el radio generado
    for index in range(len(points)):
        raux2=(points[index][0]-h)**2 +(points[index][1]-k)**2
#comparamos las diferencias de cada uno de los radios
#que generan de los puntos, si la diferencia en radios es minima 
#esos puntos 
        error+=abs(raux2-R**2)
    return error;

def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        x=decode_chromosome(F0[p])
        fitness_values[p]=f(x)

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
F1=F0[:]    

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

    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2
    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
n_gen=0;
def nextgeneration():
    global n_gen
    w.delete(ALL)
    n_gen = n_gen + 1;
    print "Generation:",n_gen
    F0.sort(cmp=compare_chromosomes)
    print "Best solution so far:"
    h,k,s=decode_chromosome(F0[0])
   
    print "h ",h," k",k," r",s
    print "error ",f(decode_chromosome(F0[0]))
    
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
    s=20
    graph_f()
    graph_population(F0,w,s,s,xo,yo,'blue')
    #graph_population(F1,w,s,s*0.5,xo,yo,'green')
    #The generation replaces the old one
    F0[:]=F1[:]

F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()

#visualization
master = Tk()

xmax=600
ymax=600
xo=300
yo=300
s=10

w = Canvas(master, width=xmax, height=ymax)
w.pack()
            
button1 = Button(master, text="Next Generation", command=nextgeneration)
button1.pack()

def graph_f():    
    w.create_line(xmax/2,0,xmax/2,ymax,fill='red')
    w.create_line(0,ymax/2,xmax,ymax/2,fill='red')
    

def graph_population(F,mycanvas,escalax,escalay,xcentro,ycentro,color):
        n_p=len(F)        

        for i in range(0,n_p): # Solo graficamos los primeros 5 chromosomas para mejor visualizacion
            h,k,r=decode_chromosome(F[i]) 

            #Se crea cada arista del cuadrado
            w.create_oval(xcentro,ycentro-s*escalay,xcentro + s*escalax,ycentro,fill='#00ffff')
            #mycanvas.create_line( xcentro,ycentro,xcentro + s*escalax,ycentro ,fill=color)
            #mycanvas.create_line(xcentro + s*escalax,ycentro ,  xcentro + s*escalax,ycentro-s*escalay ,fill=color)
            #mycanvas.create_line(xcentro + s*escalax,ycentro-s*escalay, xcentro,ycentro-s*escalay,fill=color)
            #mycanvas.create_line(xcentro,ycentro,xcentro,ycentro-s*escalay,fill=color)                
            #Se grafica el centro del cuadrado
            mycanvas.create_oval(xcentro +h*escalax,ycentro- k*escalay,xcentro +h*escalax+1,ycentro- k*escalay+1, width=5, fill='blue')


graph_f()
graph_population(F0,w,s,s,xo,yo,'blue')

mainloop()
