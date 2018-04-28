# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:22:06 2018

@author: HXT
"""
st = 'Sam print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() =='s':
        print(word)
        
##
list(range(0,11,2))
##
list_1 = [x for x in range(1,51) if x % 3== 0]
##
for num in range(1,101):
    if (num % 3==0 and num %5 ==0) : 
        print('FizzBuzz')
    elif (num %3==0):
        print('Fizz')
    elif (num%5==0):
        print('Buzz')
    else: print(num)
##
st = 'Create a list of the firsr letters of every word in this string'
list_2 = [word[0] for word in st.split()]