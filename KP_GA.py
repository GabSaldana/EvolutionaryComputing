import math
import random

#****************KP*********************************
#Max_Weight = int(raw_input())#capacity
KP_capacity=20
#Number_Elems = int(raw_input())#number of elements
Number_Elements=5
Elements=[]
for i in range(Number_Elements):
    Elements.append(map(int,raw_input().split()))
#print Elements
#************CHROMOSOME********************+*********
L_chromosome = Number_Elements
crossover_point = L_chromosome / 2
N_chromosomes=10
prob_m=0.75#probability of mutation
F0=[]
fitness_values=[]
Lwheel = N_chromosomes*10
generations = 0
#***********************++functions*********************


#** GENERATES A RANDOM CHROMOSE
#1->in 0->not in
def random_chromosome():
    global L_chromosome    
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<=0.5:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome

#******** GENERATES INITIAL POPULATION*************

for i in range(0, N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)

#** GETTING WHAT ELEMENTS WILL BE ADDED TO DE KNAPSACK
def decode_chromosome(chromosome):
    global L_chromosome
    value = []
    for p in range(L_chromosome):
        if (chromosome[p] == 1):
            value.append(p)
    return value

#** CALCULATING THE TOTAL WEIGHT OF THE GIVEN CONVINATION
#we use the indexes of the 1's elements to access the matrix
#of weights and befits 
def CalcWeight(lis):
    global Elements    
    TW = 0    
    for i in range(len(lis)):
        TW += Elements[lis[i]][1]
    return TW

#** CALCULATING THE TOTAL BENEFIT OF THE GIVEN CONVINATION
#we use the indexes of the 1's elements to access the matrix
#of weights and befits
def CalcBenefit(lis):
    global Elements    
    TB = 0    
    for i in range(len(lis)):
        TB += Elements[lis[i]][0]
    return TB

#**FITNESS FUNCTION 
#if the element fits in theknapsack we return the benefit
def f(lis):
    global KP_capacity, Elements
    fitness_val = CalcBenefit(lis)
    Wval = CalcWeight(lis)
    penalty = 0 
    #print lis
    #print "debag: ", Wval, " / ", fitness_val    
#if the total weight is bigger than the capacity     
    if (Wval > KP_capacity):   
        for i in range(Number_Elements):        
            penalty += Elements[i][0]#total benefit
        fitness_val -= penalty
        penalty = 0                
        penalty += Wval - KP_capacity
        fitness_val -= penalty         
    return fitness_val


#*************SORTING***************
def compare_chromosomes(chromosome1,chromosome2):
    vc1=decode_chromosome(chromosome1)
    vc2=decode_chromosome(chromosome2)
    fvc1 = f(vc1)
    fvc2 = f(vc2)
    if fvc1 < fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1

#*************ROULETTE WHEEL****************


def create_wheel():
    global F0,fitness_values
    #print fitness_values
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


#************PERFOMRMS THE DECODING AND CALCULATES FITNESS

def evaluate_chromosomes():
    global F0
    for p in range(N_chromosomes):
      v = decode_chromosome(F0[p])#get 1's
      fitness_values[p] = f(v)#pondering the possible solutions

#*******+CREATING NEXT GENERATION*****************
def nextgeneration():
    global generations, KP_capacity
    print ""
    print "Number of Generations: ", generations
    generations += 1
    F0.sort(cmp=compare_chromosomes)
    #print F0
    print "Max Weight: ", KP_capacity      
    print "Best solution so far:"  
    print "Fitness value for the chromosome: "
    print "f(", decode_chromosome(F0[0]), ")= ", f(decode_chromosome(F0[0]))
    print "Current value: ", CalcBenefit(decode_chromosome(F0[0])), " Current weight: ", CalcWeight(decode_chromosome(F0[0]))                                                                  
    #elitism, the two best chromosomes go directly to the next generation
    F1[0] = F0[0]
    F1[1] = F0[1]
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

F1=F0[:]
F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()

#**************MAIN****************
for i in range(50):
    nextgeneration()