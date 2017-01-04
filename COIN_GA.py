import math
import random

#****************COIN*********************************
alfa=1
beta=1
Max_Weight= 100#amount
Elements=[33,20,80]#denominations
x=8
#************CHROMOSOME********************+*********
L_chromosome=0
for i in range(0,len(Elements)):
    L_chromosome+=(int)(math.ceil((math.log(x,2))))+1
    print L_chromosome

crossover_point = L_chromosome / 2
N_chromosomes=100
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
    	if (i != 0):
        	if random.random()<=0.5:
                 chromosome.append(0)
        	else:
                 chromosome.append(1)
        else:
       	     chromosome.append(0)
    return chromosome


#******** GENERATES INITIAL POPULATION*************

for i in range(0, N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)
#print F0

#** GETTING WHAT ELEMENTS WILL BE ADDED TO DE KNAPSACK AND GENERATING THE AMOUNTS OF COINS FOR EACH DENOMINATION
def decode_chromosome(chromosome):

    #print "decodificando chromosoma"
    #print chromosome
    global L_chromosome

    combination=[]

    Acc=0
    TC=0
    coin=0
    tam=0
    k=0
    for i in range(0,len(Elements)):
        tam=(int)(math.ceil((math.log(x,2))))+1
        #print chromosome
        m=0
        coin=0
        for j in range(tam-1+k,-1+k,-1):
            #print "j:",j,chromosome[j]       
            coin+= chromosome[j]*(2**m)
            m+=1
            #print "m:",m
        
        combination.append(str(coin) + " of $" + str(Elements[i]))
        k+=tam 
        Acc+=coin*Elements[i]
        TC+=coin
                
    #print "The amount of money is: ",Acc
    #print "with: ",TC, "coins"
    
    return Acc,TC,combination

#**PUNISHMENT, FITNESS FUNCTION
def f(Acc,totalCoins):

    global Max_Weight
    f_ch =abs(Acc-Max_Weight)*alfa
    f_ch +=totalCoins*beta
    
    return f_ch


#*************SORTING***************
def compare_chromosomes(chromosome1,chromosome2):
    Acc1,TC1,combination1=decode_chromosome(chromosome1)
    Acc2,TC2,combination2=decode_chromosome(chromosome2)

    fvc1=f(Acc1,TC1)
    fvc2=f(Acc2,TC2)
    if fvc1 > fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1

#*************ROULETTE WHEEL****************

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

#************PERFOMRMS THE DECODING AND CALCULATES FITNESS

def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        Acc,totalCoins,combination=decode_chromosome(F0[p])
        fitness_values[p]=f(Acc,totalCoins)
    
    #print "fitness : ", fitness_values
	
#*******+CREATING NEXT GENERATION*****************
def nextgeneration():

    
    global generations, Max_Weight
    print ""
    print "Generation: ", generations
    generations += 1
    F0.sort(cmp=compare_chromosomes)
    Acc,totalCoins,combination=decode_chromosome(F0[0])
    print "Target Amount: $", Max_Weight
    print "Fitness value : ", f(Acc,totalCoins)
    
    print "Change ",combination
    print  "Total amount:","$",Acc, " Total Coins: ",totalCoins

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
    F0[:]=F1[:]



F1=F0[:]
F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()

#**************MAIN****************
prob_m=0.5#probability of mutation


for i in range(100):
    nextgeneration()

