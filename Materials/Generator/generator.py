# def create_cubes(n):
#     for x in range(n):
#         yield x**3

# for x in create_cubes(10):
#     print(x) 

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b