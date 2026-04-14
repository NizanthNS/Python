# Nested Loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end=" ")
#     print()


rows = int(input("Please enter a number of rows: "))
columns = int(input("Please enter a number of columns: "))
symbol = input("Please enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()