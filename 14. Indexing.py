# Indexing = Accessing elements of a sequence using [] (index operator)
#            [Start : End : Step]

c_number = "123-234-543-6532"

# print(c_number[2])
# print(c_number[: 7])
# print(c_number[7:10])
# print(c_number[5 : ])
# print(c_number[-1])
# print(c_number[::2])

last_digits = c_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

c_number = c_number[::-1]
print(c_number)
