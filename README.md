# Learn Python Course
#### Note some interesting things
-- Self-taught
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
