# primes
This was my first python script. I'm sure there is a better way to do this, but I wanted to do this by myself, so I did it this way. 
This script finds and prints prime numbers. The script needs a "primer" (pun intended) with the first few primes in it to get the script started. 
It needs to be called "primes.txt." I usually run the script and put the output into a file (possibly the same primes.txt file).

The first edition of this (created before I had a github account unfortunately) checked each number with each previously discovered prime number. 
This edition only checks the primes that are less than or equal to the square root of the number being checked.
If the reasoning for this doesn't make sense, I will briefly explain:
Every non-prime integer has to be a multiple of two or more prime numbers.
The way to test if a number is prime, is to check if it is a multiple of any other prime number.
The only way for a number to be a multiple of one number is for it to be a square of a prime number.
Every other non-prime number is a multiple of a prime number greater than the square root and a prime number less than the square root of said non-prime number.
To prove a number is not prime, we only need to find one of these numbers.
To prove a number is prime, we only need to prove the non-existence of one of these numbers.
For simplicity, we will just look for the number that is less than the square root of the number in question.
