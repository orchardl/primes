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

def isPrime(number, list, location):
        print("inside function")
        countr = 0
        myLoc = location + 1
        while countr <= myLoc:
                print("inside function while loop")
                if number % list[countr] == 0:
                        print("returning 1")
                        return 1
                countr = countr + 1
        print("returning 0")
        return 0

def GetArrayLoc(theNumber, list):
        x = 0
        while list[x]*list[x] < theNumber:
                x = x +1
        return x-1

#####test output
print("importing primes into array...")
import math
primes = readFile('primes.txt')
print("import complete")
#####

#defining variables
arrayLoc = GetArrayLoc(primes[-1],primes)
arrayLocSqr = primes[arrayLoc] * primes[arrayLoc]
nextArrayLocSqr = primes[arrayLoc + 1] * primes[arrayLoc + 1]
myNumber = primes[len(primes)-1]

#####test output
print("the variable, arrayLoc is:")
print(arrayLoc)
print("the variable, arrayLocSqr is:")
print(arrayLocSqr)
print("the variable, nextArrayLocSqr is:")
print(nextArrayLocSqr)
print("the variable, myNumber is:")
print(myNumber)
#####
#begin main
while True:
        print("you're in the outside while loop")
        while myNumber < nextArrayLocSqr:
                print("you're in the inside while loop with the number, ",myNumber)
                if isPrime(myNumber, primes, arrayLoc) == 0:
                        print("inside if... this should be a prime:")
                        primes.append(myNumber)
                        print(myNumber)
                myNumber = myNumber + 1
        print("end of inside while loop")
        arrayLoc = arrayLoc + 1
        arrayLocSqr = primes[arrayLoc] * primes[arrayLoc]
        nextArrayLocSqr = primes[arrayLoc + 1] * primes[arrayLoc + 1]
        print("the variable, arrayLoc is:")
        print(arrayLoc)
        print("the variable, arrayLocSqr is:")
        print(arrayLocSqr)
        print("the variable, nextArrayLocSqr is:")
        print(nextArrayLocSqr)
        print("the variable, myNumber is:")
        print(myNumber)


#end
