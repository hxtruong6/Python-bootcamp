# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:19:58 2018

@author: HXT
"""

def say_hello(name = 'NAME'):
    print('hello ' + name)
    
say_hello()
say_hello('truong')

##
def add(n1,n2):
    return n1+n2
result = add(40,50)

## find word 'dog' in string
def dog_check(mystring):
    if 'dog' in mystring.lower():
            return True
    return False

print(dog_check("Ohh, this string doesn't has word dog."))
print(dog_check("dog"))
## Warmup section
#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(num1, num2):
    if (num1 % 2 ==0 and num2 %2 ==0) :
        return min(num1,num2)
    else:
        return max(num1,num2)
    
### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(mystring):
    return mystring.split()[0][0] == mystring.split()[1][0]

### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(num1, num2):
    return (num1+num2 == 20 or (num1==20 or num2 == 20))

## Level 1
### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(mystring):
    if (len(mystring) >3):
        return mystring[:3].capitalize() + mystring[3:].capitalize()
    else:
        return "Not enough letters in string"

### MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(mystring):
    return ' '.join(mystring.split()[::-1])

### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almaost_there(n):
    return ((abs(n-100)<=10) or (abs(200-n)<=10))

## Level 2    
### FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def find_33(listInt):
    for i in range(0,len(listInt)-1):
        if (listInt[i:i+2] == [3,3]):
            return True
    return False

### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(mystring):
    res = ""
    for letter in mystring:
        res+= letter *3
    return res
    
### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def back_jack(num1, num2, num3):
    res = num1 + num2 +num3
    if ((res>21) and (num1 ==11 or num2 ==11 or num3== 11)):
        res-=10;
    if (res<=21):
        return res 
    else: 
        return 'BUST'

### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(nums):
    section69 = False
    res = 0
    for num in nums:
        if (num == 6 and not section69):
            section69 = True
        elif num == 9 and section69: 
            section69 = False
        elif not section69:
            res+= num            
    return res

## Challenging problems
### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    code = [0,0,7, '#']
    for num in nums:
        if (num==code[0]):
            code.remove(0)
    return len(code)==1

### COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def is_prime(k):
    if (k<2): return False
    n = k;
    n = int(n**0.5)
    for i in range(2, n+1):
        if ( k % i == 0): return False
    return True
        
def count_primes(n):
    count =0
    for k in range(2,n+1):
        if (is_prime(k)):
            count+=1;
            print(k)
            
    return count;
### solution 2
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

