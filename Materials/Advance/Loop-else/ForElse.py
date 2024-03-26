# the similar while.. else
"""
a list contains a number divide divisor
if not add divisor to list
"""
def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
           return item
   
    items.append(divisor)
    return divisor

items = [2,25,9]
divisor = 12 

dividend = ensure_has_divisible(items, divisor)

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))