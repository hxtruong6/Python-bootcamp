"""
try:
    # this code might raise an exception
    do_something()
except ValueError:
    # ValueError caught and handled
    handle_value_error()
else:
    # No exception was raised
    # We know that do_something() succeeded, so
    do_something_else()
"""
filename = "file.txt"
try: 
    f = open(filename, 'r')
except OSError:
    print("File could not be opened for read")
else:
    # now we're sure the file is open
    print("Number of lines", sum(1 for line in f))
    f.close()