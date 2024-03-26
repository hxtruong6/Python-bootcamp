# map()
temps = [0, 22.5, 40, 100]
tm = list(map(lambda x: (9/5)*x + 32, temps))
print(tm)

# map() with multiple iterables
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

ta = list(map(lambda x,y:x+y,a,b))
print(ta)

# Now all three lists
tb = list(map(lambda x,y,z:x+y+z,a,b,c))
print(tb)

from functools import reduce

# reduce()
lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)
#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b
#Find max
reduce(max_find,lst)

# Zip()
x = [1,2,3]
y = [4,5,6]

# Zip the lists together
list(zip(x,y)) # only zip the shortest length list
# zip dic
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

list(zip(d1,d2))
# enumrate 
lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)

months = ['March','April','May','June']
list(enumerate(months,start=3))

# Create 2+3j
complex(2,3)
complex("12 + 3.4j")


### Assignment
#Problem 1
##Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.
##The function will have an input of a string, and output a list of integers.
def word_lengths(phrase):
    return list(map(len,phrase.split()))
#Problem 2
##Use reduce() to take a list of digits and return the number that they correspond to. For example, [1, 2, 3] corresponds to one-hundred-twenty-three. 
##Do not convert the integers to strings!
from functools import reduce

def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)

#Problem 3
##Use filter() to return the words from a list of words which start with a target letter.
def filter_words(word_list, letter):
    return list(filter(lambda word: word[0]== letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')

#Problem 4
#Use zip() and a list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:
def concatenate(L1, L2, connector):
    return list(str(t[0]+connector+t[1]) for t in zip(L1, L2))

#Problem 5
#Use enumerate() and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.
def d_list(L):
    return {key:val for val, key in enumerate(L)}
    
#Problem 6
##Use enumerate() and other skills from above to return the count of the number of items in the list whose value equals its index.
from functools import reduce
def count_match_index(L):
    #return len(list(filter(lambda x: x == True, list(num == val for num, val in enumerate(L)))))
    return len([num for count,num in enumerate(L) if num==count])

