def is_comment(item):
    '''
        rely if item is a comment
    '''
    return isinstance(item,str) and item.startswith('#')

def execute(program):
    # get all item is not comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else: # no break
        print("Empty program")
        return
    
    # evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending) # execute all item in pending with operator is item (+,-,*,/,..)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else: #nobreak
        print("Program successful.")
        print("Result: ", pending)
    
    print("Finished!")




if __name__ == '__main__':
    import operator

    program = list(reversed((
        "#A short stack program to add",
        "#and multiply some constants",       
        5,
        2,
        operator.add,
        3,
        operator.mul,
        3,
        operator.lshift
    )))
    execute(program)