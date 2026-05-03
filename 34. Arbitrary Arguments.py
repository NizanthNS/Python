# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional, 2. DEFAULT 3. keyword, 4. ARBITRARY


# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,2,4,5,6))

# def display_name(*args):
#     for arg in args:
#         print(arg, end = " ")
#
# display_name("Niz", "NS")

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address (street = "9173 TPM St.",
#                apartment = "152",
#                city = "Pittsburgh",
#                state = "CA",
#                zip_code = "9410")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # for value in kwargs.values():
    #     print(value, end = " ")
    if "apartment" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
    elif "pbox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pbox')}")
    else :
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip_code')}")

shipping_label("Dr.", "Levi", "Ackerman", "AOT",
                street = "9173 TPM St.",
                pbox = "PO Box #3423",
                city = "Pittsburgh",
                state = "CA",
                zip_code = "9410")