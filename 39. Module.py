# Module = A file containing code you want to include in your program
#          Use 'import' to include a module (built-in your own)
#          Useful to break up a large program reusable separate files

# print(help("modules"))

# print(help("math"))

# import math as m
# from math import pi
# print(pi)
# from math import e

# a, b, c, d = 1, 2, 3, 4
#
# print(m.e ** a)
# print(m.e ** b)
# print(m.e ** c)
# print(m.e ** d)

import example

# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
result = example.area(3)

print(result)