# Learn Python Course
#### Note some interesting things
-- Self-taught
## Jupyter
- Start type: 'jupyter notebook'
## Python Object and Data Structure Basics
- Power in number: ** . Ex: 2**4 = 2^4 = 16
- Negative index in string. Ex: str= 'Truong' -> str[-1] = 'g' mean this last character of string
- Get character in string: str[START:END:STEP]. Note: not including character[END]
- Function Split:
  * str.split() -> split each word in a string as array
  * str.split('i') -> split until meet character 'i'. Ex: str = "Hello! This is an bird." -> 'Hello! Th', 's ', 's an b', 'rd.'
- Format in print: use '{}'.format  to print string/result follow defined format
- Set just get the unique element. Ex: myset = set(); myset.add(element)
- IO file
  * open(), read()
  * when read() file, the cursor will be moved the end of file. Use seek(int) to set again cursor
  * read() evert line: readlines() -> list string follow each line in file
  * with open('myfile.txt') as my_new_file:
      contents = my_new_file.read()
      -> file open and close automatically, the contents in file will independence with file
## Statements
- Key word 'enumerate' use show (index, result) in loop
- Key word 'Zip' use zip lists together follow index
## Function
- * args : list of parameter when pass to Function
- ** kwargs:  return a dictionary  
- map: use match between list argument with parameter of function. Ex: map(square, my_nums) -- square is function, my_nums is list number
- filter: use filter element follow condition. Ex: filter(condition,list)
- lamda parameter:return. Ex: lamda num:num%2==0
- Scope:
  * use 'global' in def to get value of global variable (re-assignment)
  * code clearly: x = function(x) when re-assignment variable; def function(x): #code -> return x
## OOP
- Init function: def __init__(self, parameterm,...)
- Inherit: class Dog(Animal): -> Dog Inherit from Animal
  * Call again class parent: def __init__(self): Animal.__init__(self)
  * If call a function which is not define in children class, it will inherit form parent class. In contract, children will use own function if it has same name.
  * Polymorphism: A class have many parents class.
- Special method in class:
  * __str__(self): call str(name class) to describe what this class is.
  * __len__(self): return length of class (anything you want)
  * __del__(self) -- del class: use to delete from memory of computer
## Modules and Packages
- if __name__ == "__main__": check if this file .py is run directly
## Unit Test
## Map(), reduce(), filter()
### Reduce()
- from functools import reduce
### Zip()
- zip() makes an iterator that aggregates elements from each of the iterables.
- Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
- zip() is equivalent to:
```
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
```
- zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables.
### Enumerate()
- In this lecture we will learn about an extremely useful built-in function: enumerate(). Enumerate allows you to keep a count as you iterate through an object. It does this by returning a tuple in the form (count,element). The function itself is equivalent to:
```
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```
### all() and any()
- all() and any() are built-in functions in Python that allow us to conveniently check for boolean matching in an iterable. - all() will return True if all elements in an iterable are True. It is the same as this function code:
```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```
- any() will return True if any of the elements in the iterable are True. It is equivalent to the following function code:
```
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```
### complex()
- complex() returns a complex number with the value real + imag*1j or converts a string or number to a complex number.
- If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.
- If you are doing math or engineering that requires complex numbers (such as dynamics, control systems, or impedance of a circuit) this is a useful tool to have in Python.
```
  # Create 2+3j
  complex(2,3)
```
## Decorator
- Use symbol '@' to execute the function.
## Generator
- Advantage: the generator compute one value and waits until the function are called next
- Use keyword: 'yeild' to return a value which was computed when user call
- 'next(...)' to get next value in yeild
- 'inter(...)' to get next value in normal variable
- Use generator when only get the needed value. Don't need to run whole of function
- Problem: Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
    * If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator. (Multiple answers are acceptable here!)
## Advance python modules
### Counter
- Use to count the dup licate element in a list
- Useful in process natural language 
- Code:
```
    from collections import counter
    _list = [1,2,4,3,5,2,5,2,5,7,3]
    Counter(_list)
```
- Common methods:
    * sum(c.values())
    * c.clear()
    * list(c)   // is considered as set
    * c.items()
    * ...
### Default dict
- Code:
```
    from collections import defaultdict
    d = {}
    d['one] # -> error
    d = defaultdict(object) 
```
- Use it to never raise a key error -> return a default value
### Ordered dict
- Code:
```
    d = {}
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    # a normal dictionary
    from collections import OrderedDict
    d1 = OrderedDict()
    d1['b'] = 2
    d1['a'] = 1
    d1['c'] = 3
    # an ordred dict -> it will not change the position in dict
```
- Keeping position of elements in dict as the initiate dict. It's not change dict follow anlpha sort
### Name Tupe
- Show informations for a tuple (it's too hard to remember when coding)
- Structure: object = namedtuple('name','variable1 variable2 variable3')
- Code:
```
    from collections import namedtuple

    Dog = namedtuple('Dog', 'age breed name')
    sam = Dog(age = 12, breed = 'Lab', name= 'Sammy' )
    sam
    sam.age #age is subclass of tuple(Dog)

```
### Datetime
- Time: datetime.time
    * datetime.time(minutes,seconds,microseconds)
    * datetime.time.min 
    * datetime.time.max
    * datetime.time.resolution
- Date: datetime.date.resolution
### Python debugger
```
    import pdb
    pdb.set_trace()
```
### Regular Expressions
- [a-z]+ : get character a->z and add any another character
### String IO
### Number
- bin
- hex
- pow(a,b) = a**b
- pow(a,b,c) = a**b % c
- abs
- round(a,b): round b digits after comma
### String
- str.find('a'): position of str
- str.center(20, 'z'): put str at center then add z to length of str is 20
- print("abc/tde) = "abc/tde".expandtabs()
- str.isalnum() : check string is alphal numeric
- str.isalpha() : check string is alphabet
- str.partition('a'): just split at begining of str
