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