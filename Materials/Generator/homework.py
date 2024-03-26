# 1.Create a generator that generates the squares of numbers up to some number N
def generates(N):
    for i in range(N):
        yield i**2



# 2.Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
import random

def rand_num(low,high, n):
    for x in range(n):
        yield random.randint(low,high)
# 3.Use the iter() function to convert the string below into an iterator:
def convert_string_to_iterator(s):
    _iter = iter(s)
    return _iter

# 4 
"""
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

gencomp is a generator comprehension. It only return a value when a line code excute/call it
Note: A list comprehension uses bracket [] instead of using bracket () likes a generator comprehension
"""
#########
if __name__== '__main__':
    # 1
    # for x in generates(10):
    #     print(x)
    # 2
    for x in rand_num(1,100, 10):
        print(x)