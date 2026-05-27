# Decorator = A function that extends the behavior of Another function
#             w/o modifying the base function as an argument to the decorator
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("**Adding sprinkles 🥗**")
        func(*args, **kwargs)
    return wrapper

def add_fudges(func):
    def wrapper(*args, **kwargs):
        print("*Adding fudges 🍫 *")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudges
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("Cherry")