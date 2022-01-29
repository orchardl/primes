#setting up our environment
import math
import time #this is for testing to determine the best number of processes to run on my machine
import multiprocessing

# Reads in the file in the argument
def readFile(fileName):
        myNums = []
        fileObj = open(fileName, "r") #opens the file in read mode
        while fileObj:
                line = fileObj.readline()
                if line == "":
                        break
                value = int(line)
                myNums.append(value)
        fileObj.close()
        return myNums

def getInitialNumofReps(initialPrimes):
        myPrime = 0
        counter = 0
        lastNumber = initialPrimes[-1]
        while math.sqrt(lastNumber) > myPrime:
                counter = counter + 1
                myPrime = primes[counter]
        return counter + 1

# This function decides how many prime numbers need to be checked
def getNumReps(theNumber, currentNumReps, thePrimes):
        if thePrimes[currentNumReps-1]*primes[currentNumReps-1] > theNumber:
                return 0
        return 1

# This is the critical function that decides if the number is a prime or not
def isPrime(number, list, reps):
        countr = 0
        while countr < reps:
                if number % list[countr] == 0:
                        return 1
                countr = countr + 1
        return 0

#this is setting up our variables
primes = readFile('primes.txt') #the primes array gets all the primes in the file
numReps = getInitialNumofReps(primes) #numReps determines how many primes to check
myNumber = primes[len(primes)-1] + 1 #this is the first number we'll be checking
numIter = input("How many more numbers do you want me to check for primes?")

#begin main
#0 means to add it to the text file
#1 means it is not prime, or it is already in the file
#the while loop cycles through every number starting with "myNumber"

start = time.time()
for _ in range(numIter):
        if isPrime(myNumber, primes, numReps) == 0:
                primes.append(myNumber)
                print(myNumber)
        myNumber = myNumber + 1
        numReps = numReps + getNumReps(myNumber, numReps, primes)
finish = time.time()
print("---%s seconds ---" % (start - finish))
