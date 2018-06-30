# the similar while.. else
"""
a list contains a number divide divisor
if not add divisor to list
"""
 

for item in items:
    if item % divisor == 0:
        found = item
        break
else: # no break
    items.append(divisor)
    found = divisor

items = [2,25,9]
divisor = 12

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))