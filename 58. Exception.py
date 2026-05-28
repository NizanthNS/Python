# exception =  An event that interrupts the flow of a program
#              (ZeroDivisionError, TypeError, ValueError)
#              1. try, 2.except, 3. finally

# 1 / 0      = ZeroDivisionError
# 1 + "8"    = TypeError
# int("Niz") = ValueError

try:
    number = int(input("Enter a number: "))
    print(1 / number)

except ZeroDivisionError:
     print("Learn Math you Moron, Numbers are not divisible by zero.")
except ValueError:
     print("Enter only numbers please.")
except Exception:
    print("Something went wrong.")
finally:
    print("Goodbye!")
