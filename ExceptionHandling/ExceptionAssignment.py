# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 05:47:44 2018

@author: HXT
"""

# 1 
try: 
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Type error: 'int' pow() 'str'")
    
# 2 
try: 
    x = 5
    y = 0
    z = x/y
except:
    print("Divison by zero")
finally:
    print("All done!")
    
# 3
while True:
    try:
        x = int(input("Enter a number: "))
    except:
        print("Error: Please enter a number!")
        continue
    else:
        print(f"Thank you! Your result is {x**2}")
        break;
    