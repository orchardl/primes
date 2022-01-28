import math

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

def getNumReps(theNumber, currentNumReps, thePrimes):
        if thePrimes[currentNumReps-1]*primes[currentNumReps-1] > theNumber:
                return 0
        return 1

def isPrime(number, list, reps):
        countr = 0
        while countr < reps:
                if number % list[countr] == 0:
                        return 1
                countr = countr + 1
        return 0


primes = readFile('primes.txt')
numReps = getInitialNumofReps(primes)

#0 means to add it to the text file
#1 means it is not prime, or it is already in the file

myNumber = primes[len(primes)-1]
while True:
        if isPrime(myNumber, primes, numReps) == 0:
                primes.append(myNumber)
                print(myNumber)
        myNumber = myNumber + 1
        numReps = numReps + getNumReps(myNumber, numReps, primes)
