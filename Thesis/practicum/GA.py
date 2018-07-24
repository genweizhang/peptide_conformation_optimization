#basic framework of GA for thesis project
#
#Author: Genwei Zhang
#Date: 06/28/2018

#import python libraries
import copy
import math
from random import Random
import numpy as np
#import progressbar

#to setup a random number generator, we will specify a "seed" value in order to reproduce the result.
seed = 123
RanGenerator = Random(seed)

angles = 44    #this defines total angle numbers in the whole search space
lowerbound = -180  #the lower bounds for phi, psi, chi angles
upperbound = 180   #the upper bounds for psi, psi, chi angles



#create a chromosome randomly within the designated range
def createChromosome(dim, lowBnd, upBnd):   
    x = []
    for i in range(dim):
        x.append(RanGenerator.uniform(lowBnd,upBnd))   #create a solution randomly
        
    return x

# to initialize the  population

popsize = 50     #size of the GA population

def initializePopulation(): 
    population = []
    populationFitness = []
    
    for i in range(popsize):
        population.append(createChromosome(angles,lowerbound, upperbound))
        populationFitness.append(evaluate(population[i]))

    # zip and sort    
    Ziptogether = zip(population, populationFitness)
    pop_values = sorted(Ziptogether, key=lambda Ziptogether: Ziptogether[1])
    
    #the return object is a sorted list of tuples: 
    #the first element of the tuple is the chromosome; the second element is the fitness value
    
    return pop_values    


#function to evaluate the Schwefel Function for d dimensions
def evaluate(x):  

    from compute_energy_amber import get_total_energy      
    
    val = get_total_energy(x)
    
    return val   

#implement a linear crossover
crossover_rate = 0.8

def crossover(x1,x2):
    
    d = len(x1) #dimensions of solution
    
    #choose crossover point 
    
    #we will choose the smaller of the two [0:crossOverPt] and [crossOverPt:d] to be unchanged
    #the other portion be linear combo of the parents
        
    crossOverPt = RanGenerator.randint(1,d-1) #notice I choose the crossover point so that at least 1 element of parent is copied
    
    beta = RanGenerator.random()  #random number between 0 and 1
        
    #note: using numpy allows us to treat the lists as vectors
    #here we create the linear combination of the soltuions
    # this is necessary for continuous space, maybe ignored in case of binary solutions.
    new1 = list(np.array(x1) - beta*(np.array(x1)-np.array(x2))) 
    new2 = list(np.array(x2) + beta*(np.array(x1)-np.array(x2)))
    
    # generate a random number between 0 and 1, crossover occurs with a probability of the crossover rate
    randnumber = RanGenerator.random()
    if randnumber <= crossover_rate:
        #the crossover is then performed between the original solutions "x1" and "x2" and the "new1" and "new2" solutions
        if crossOverPt<d/2:    
            offspring1 = x1[0:crossOverPt] + new1[crossOverPt:d]  #note the "+" operator concatenates lists
            offspring2 = x2[0:crossOverPt] + new2[crossOverPt:d]
        else:
            offspring1 = new1[0:crossOverPt] + x1[crossOverPt:d]
            offspring2 = new2[0:crossOverPt] + x2[crossOverPt:d]
    else:
        # no crossover happening, offspring simply equal to the new1 and new2
        offspring1 = new1
        offspring2 = new2      
    
    return offspring1, offspring2  #two offspring are returned 

          
  
#performs tournament selection; k chromosomes are selected (with repeats allowed) and the best advances to the mating pool
#it returns the mating pool with size equal to the initial population
def tournamentSelection(pop,k):
    
    #randomly select k chromosomes; the best joins the mating pool
    matingpool = []
    
    while len(matingpool)<popsize:
        
        ids = [RanGenerator.randint(0,popsize-1) for i in range(k)]
        competingpool= [pop[i][1] for i in ids] 
        # compare the fitness values and return the chromosome ID with smaller fitness
        bestID=ids[competingpool.index(min(competingpool))]
        matingpool.append(pop[bestID][0])

    return matingpool
    
#function to mutate solutions

mutation_rate = 0.1

def mutate(x):
    
    # mutation probability
    q = mutation_rate
    # generate a random number between 0 and 1, mutation occurs with a probability of the mutation rate
    randnumber = RanGenerator.random()
    if randnumber <= q:
        mutateposition = RanGenerator.randint(0,angles-1)
        mutateToposition= RanGenerator.randint(0,angles-1)
        if randnumber <= q/2:
            # mutate to a component within this x
            x[mutateposition] = x[mutateToposition]
        else:
            # mutate to a random number between -180 and 180
            x[mutateposition] = RanGenerator.uniform(lowerbound, upperbound)
        
    return x
        
#insertion step
def insert(pop,kids):

    #Probably replacing the previous generation completely is probably a bad idea 
    # The elitism we used here is: keep top 50% of pop and top 50% of kids  
    mix = []
    for i in range (len(pop)/2):
        mix.append(kids[i])
        mix.append(pop[i])
    return mix
    
def breeding(matingPool):
    #the parents will be the first two individuals, then next two, then next two and so on
    
    children = []
    childrenFitness = []
    for i in range(0,popsize-1,2):
        child1,child2=crossover(matingPool[i],matingPool[i+1])
        
        child1=mutate(child1)
        child2=mutate(child2)
        
        children.append(child1)
        children.append(child2)
        
        childrenFitness.append(evaluate(child1))
        childrenFitness.append(evaluate(child2))
        
    Ziptogether = zip(children, childrenFitness)
    pop_values = sorted(Ziptogether, key=lambda Ziptogether: Ziptogether[1])
        
    #the return object is a sorted list of tuples: 
    #the first element of the tuple is the chromosome; the second element is the fitness value
    #for example:  popVals[0] is represents the best individual in the population
    #popVals[0] for a 2D problem might be  ([-70.2, 426.1], 483.3)  -- chromosome is the list [-70.2, 426.1] and the fitness is 483.3
    
    return pop_values


    
#perform a simple summary on the population: returns the best chromosome fitness, the average population fitness, and the variance of the population fitness
def summaryFitness(pop):
    a=np.array(list(zip(*pop))[1])
    return np.min(a), np.mean(a), np.var(a)


    
    

###
##        ~~~~~~~~~~~~~~~~~~~~~~~~~
##       ||                       ||
##       ||   The GA Main code    ||
##       ||                       ||
##        ~~~~~~~~~~~~~~~~~~~~~~~~~ 


#define number of GA generations
generations = 50    

#initialize the whole population
Population = initializePopulation()

# f.write(str(Population)+ "\n")
# create a progress bar to monitor the optimization process speed
#bar=progressbar.ProgressBar(maxval=Generations, widgets=[progressbar.Bar('=', '[', ']',), ' ', progressbar.Percentage()])
#bar.start()

#f = open('Best_pose_coord_44_200pops_150.txt', 'w')
for j in range(generations):

    mates=tournamentSelection(Population,2)
    Offspring = breeding(mates)
    Population = insert(Population, Offspring)
    minVal,meanVal,varVal=summaryFitness(Population)
    
    #bar.update(j+1)
    
    # save to file
    #f.write("This is step "+ str(j+1) + ", and current best value found is: "+ str(Population[0][1]) + "\n")
    
    # print on screen
    print("Step "+  str(j) + ", current best value found is:", Population[0][1])
    #if Population[0][1]<0:   # another stopping criteria
    #    break

#bar.finish()
print ("the fitness summary of the pop is: ", summaryFitness(Population))

print ("The best solution found is:", Population[0])

#optional: you can output the final coord results to a file    

#f.write("The final best pose coord is: " +str(Population[0][0])+ "\n")

#f.close() 