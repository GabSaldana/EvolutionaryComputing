
from Tkinter import *
import math
import random

def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.5:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome

def decode_float(lowerlimit, upperlimit, bits):
    L_bits = len(bits)
    N_chains = 2**L_bits

    value=0
    for p in range(L_bits):
        value+=(2**p)*bits[-1-p]
    return lowerlimit+(upperlimit-lowerlimit)*float(value)/(N_chains-1)
def decode_chromosome(chromosome):
    global L_chromosome,N_chains
    h = decode_float(0,5, chromosome[:Nbits_h])
    k = decode_float(0,5, chromosome[Nbits_h:Nbits_h+Nbits_k])
    R = decode_float(0,10, chromosome[Nbits_h+Nbits_k:])
    return h,k,R

def f(x):
    global points
    L_points=len(points)
    #x = h,k,R
    h, k, R=x
    error=0
    
    #x-> points[][0]
    #y-> points[][1]
    maxX= points[0][0]
    maxY= points[0][1]
    minX= points[0][0]
    minY= points[0][1]
    #para X
    for i in range(0,L_points):
        if maxX < points[i][0] :
           maxX = points[i][0]
    for i in range(0,L_points):
        if minX > points[i][0] :
           minX = points[i][0]           
    #para Y
    for i in range(0,L_points):
        if maxY < points[i][1] :
           maxY = points[i][1]
    for i in range(0,L_points):
        if minY > points[i][1] :
           minY = points[i][1]
    A=maxX- minX
    B=maxY- minY
    
    
    L=max(A,B)
    h=L/2
    k=L/2
    #print "A",A, " B", B," L",L


    hch, kch, Lch=x #solucion del cromosoma
    #print "sizech",Lch, "hch ",hch," kch ",kch

    error+=abs(L- Lch )
    error+=abs(h- hch )
    error+=abs(k- kch )
    #print "Error",error

    return error
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
def nextgeneration():
    w.delete(ALL)
    F0.sort(cmp=compare_chromosomes)
    print "Best solution so far:"
    h,k,s=decode_chromosome(F0[0])
    

    print "h ",h," k",k," s",s
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
    graph_population(F0,w,s,s,xo,yo,'red')
    #graph_population(F1,w,s,s*0.5,xo,yo,'green')
    #The generation replaces the old one
    F0[:]=F1[:]




points = [ (0,3) , (10,6) , (3,10)]

Nbits_h =8
Nbits_k=8
N_bits_r=8
L_chromosome = Nbits_h + Nbits_k + N_bits_r


prob_m=0.5      #probability of mutation
N_chromosomes=10 #Number of chromosomes


N_chains=2**L_chromosome
crossover_point=L_chromosome/2

a=-20
b=20





F0=[]
fitness_values=[]
 
for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)

Lwheel=N_chromosomes*10
F1=F0[:]    
F0.sort(cmp=compare_chromosomes)

evaluate_chromosomes()






#visualization
master = Tk()

xmax=600
ymax=600

xo=300
yo=300

s=20

w = Canvas(master, width=xmax, height=ymax)
w.pack()

            
button1 = Button(master, text="Next Generation", command=nextgeneration)
button1.pack()

N=100


def graph_f():    
    w.create_line(xmax/2,0,xmax/2,ymax)
    w.create_line(0,ymax/2,xmax,ymax/2)
    

def graph_population(F,mycanvas,escalax,escalay,xcentro,ycentro,color):
        

        for i in range(0,5): # Solo graficamos los primeros 5 chromosomas para mejor visualizacion
            h,k,s=decode_chromosome(F[i]) 

            #Se crea cada arista del cuadrado
            mycanvas.create_line( xcentro,ycentro,xcentro + s*escalax,ycentro ,fill=color)
            mycanvas.create_line(xcentro + s*escalax,ycentro ,  xcentro + s*escalax,ycentro-s*escalay ,fill=color)
            mycanvas.create_line(xcentro + s*escalax,ycentro-s*escalay, xcentro,ycentro-s*escalay,fill=color)
            mycanvas.create_line(xcentro,ycentro,xcentro,ycentro-s*escalay,fill=color)                
            #Se grafica el centro del cuadrado
            mycanvas.create_oval(xcentro +h*escalax,ycentro- k*escalay,xcentro +h*escalax+1,ycentro- k*escalay+1, width=5, fill='blue')

            


graph_f()
graph_population(F0,w,s,s,xo,yo,'red')
F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()



mainloop()
