# Advance Python
- __<method-name>__ : say "DUNDER <method-name>" (Dunder = underscore-underscore)
### Loop..else
- while...else
- for...else
- => refactor. Extract mothod
- try..else
- Emulating Switch ( switch not support in python)
```
    index
    dic = {
        'a': func1,
        'b': func2,
        'c': func3,
        'd': func4
    }

    try:
        execute_func = dic[index]
    except Error:
        print("Some thing")
    else:
        res = execute_func()

```
- Dispatching_on_Type 
### Byte-oriented-Programming
### Object-internals-and-Customs-attributes
- __dict__ in class of Python is as a dictionary contain all attribute which are defined by programer
- __dir__ use to show all attribute of class
- Overriding
    * __getarrr__(): invoked AFTER  requested attribute/property not found by normal lookup
    * __getattrubute__(): involed INSTEAD OF normal lookup
    * __setattr__(): raise an error not allow set value
- Pitfalls __getattr__
- Overriding __delattr__()
- Use Vars() to Access __dict__
- A dict in python has size 288 bytes
- __slots__ = ['var1', 'var2', 'var3'] : allocate fix memory. Not allow add more variable
### Descriptors
```
    property(fget= None, fset= None, fdel= None, doc= None)-> property attribute
    class C(object):
        def getx(self): return self._x
        def setx(self): self._x = value
        def delx(self: del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")
```
- Implementing a descriptor
- Calling descriptor on Classes
### Creation
- Inherited __new__() allocated the object which is passed to __init__() as self
- Customising allocation
    * interning: Only use for immutable value type

    



