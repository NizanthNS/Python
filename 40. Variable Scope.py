# Variable Scope = Where a variable is visible and accessible
# Scope resolution = (LEGB) Local - > Enclosed - > Global - > Built-in

# def function1():
#     x = 1
#
#     def function2():
#         print(x)
#     function2()
#
# function1()

# def function1():
#     print(x)
#
# def function2():
#     print(x)
#
# x =3
#
# function1()
# function2()

from math import e

def function1():
    print(e)

e = 3

function1()