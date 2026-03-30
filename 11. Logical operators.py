# Logical Operators = Evaluate multiple conditions (OR, AND, NOT)
#                     OR = At least one condition must be true
#                     AND = Both conditions must be True
#                     NOT = Inverts the condition (NOT False, NOT True)
from selectors import SelectSelector

# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#    print("The event is cancelled")
# else:
#    print("The event is scheduled")


# temp = 20
# is_sunny = True
#
# if temp >= 28 and is_sunny:
#     print("Its Hot outside")
#     print("Its Sunny")
# elif temp <=0 and is_sunny:
#     print("Its COLD outside")
#     print("Its Sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("Its WARM outside")
#     print("Its Sunny")

temp = -1
is_sunny = False

if temp >= 28 and not is_sunny:
    print("Its Hot outside")
    print("Its Cloudy")
elif temp <=0 and not is_sunny:
    print("Its COLD outside")
    print("Its Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("Its WARM outside")
    print("Its Cloudy")
