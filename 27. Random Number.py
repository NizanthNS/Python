import random

# print(help(random))

low = 1
high = 100
options = ("Rock", "Paper", "Scissors")
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)

# print(number)
# print(option)

print(cards)