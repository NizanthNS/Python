# Concession Stand Program
# Dictionary {key : value}

menu = {"Pizza" : 5.00,
        "Burgers" : 3.50,
        "Fries" : 2.00,
        "Nachos" : 1.50,
        "Soda" : 1.00,
        "Cheese" : 1.00,
        "Lemonade" : 1.50,
        "Puffs" : 2.50,
        "Sandwich" : 3.00,
        "PoP corn" : 7.00}


cart = []
total = 0

print("----------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------")

while True:
    food = input("Select a item (q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end =" ")

print()
print(f"Total: {total:.2f}")