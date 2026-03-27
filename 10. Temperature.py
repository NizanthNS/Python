unit = input("Is this temperature in celsius or fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The temperature is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in celsius is: {temp}°C") # 0176 or 0178
else:
    print(f"{unit} is not a valid unit")