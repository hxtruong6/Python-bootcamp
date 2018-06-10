# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:42:59 2018

@author: HXT
"""
# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4/3)*3.14*(rad**3);

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return num in range(low,high + 1)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    upCount = 0
    lowCount = 0
    for letter in s:
        if (letter.isupper()): 
            upCount+=1
        elif letter.islower():
            lowCount+=1
    
    print(f"No. of Upper case characters : {upCount}")
    print(f"No. of Lower case Characters : {lowCount}")
    
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    print(set(lst))
    
# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    res = 1
    for num in numbers:
        res = res* num
    return res

# Write a Python function that checks whether a passed in string is palindrome or not.
def palindrome(s):
    return s[0:int(len(s)/2):1]==s[:int(len(s)/2) - (len(s)-1)%2 :-1]

# Write a Python function to check whether a string is pangram or not.
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str_1 = set(str1)
    for letter in alphaset:
       if (letter not in str_1):
           return False
    return True









