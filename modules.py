# module = a file containing code you want to include in your program
# use 'import' to include a module (build-in or your own)
# useful to break up a large program into reusable seperate files

#print(help("modules"))
#print(help("math"))

#import math
#print(math.pi)

#import math as m
#print(m.pi)

#from math import pi 
#could result in conflicts
#print(pi)
#from math import e
#a, b ,c ,d, e = 1, 2, 3, 4, 5
#print(e ** a)
#print(e ** b)
#print(e ** c)
#print(e ** d)
#print(e ** e)

import math
a, b ,c ,d, e = 1, 2, 3, 4, 5
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

import example
result1 = example.pi
result2 = example.square(3)
result3 = example.cube(3)
result4 = example.circumference(3)
result5 = example.area(3)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

#print(help(example))