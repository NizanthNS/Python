# Dictionary = A collection of {key : Value} pairs
#              Ordered and changeable. No duplicates

capitals = {"USA"    : "Washington D.C",
            "UK"     : "London",
            "India"  : "New Delhi",
            "Japan"  : "Tokyo",
            "Russia" : "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
# print(capitals.get("UK"))
# print(capitals.get("India"))
# print(capitals.get("Japan"))
# print(capitals.get("Russia"))

# if capitals.get("China"):
#     print("That Capital Exists")
# else:
#     print("That Capital Does Not Exist")

# capitals.update({"Germany" : "Berlin"})
# capitals.update({"India" : "Mumbai"})
# capitals.pop("Russia")
# capitals.popitem()
# capitals.clear()

# print(capitals)

# keys = capitals.keys()
# print(keys)
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)
# for item in capitals.items():
#     print(item, end = " ")

for key, value in capitals.items():
    print(f"{key}: {value}")