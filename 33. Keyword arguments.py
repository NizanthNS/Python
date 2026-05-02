# default arguments = An argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. DEFAULT 3. keyword, 4. arbitrary

# def hello(greeting, title, firstname, lastname):
#     print(f"{greeting} {title}{firstname} {lastname}")
#
# hello(title = "Mr.", firstname = "Niz", lastname = "NS", greeting = "Hello")

# for x in range(1,11):
#     print(x, end = " ")

# print("1","2","3","4","5","6","7","8","9", sep = "-")

def get_phone(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}-{last}"

phone_number = get_phone(country_code = "91", area_code = "88", first = "0736", last = "0610")
print(phone_number)