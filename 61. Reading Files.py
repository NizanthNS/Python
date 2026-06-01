# Reading Files Python (.txt, .json, .csv)

# file_path = "D:/Test/Emp.txt"
#
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")

# import json
#
# file_path = "D:/Test/Emp.json"
#
# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content [0]["Department"])
        # for employee in content:
        #     print(employee ["Department"])
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")
# except json.JSONDecodeError:
#     print("Invalid JSON format")
# except TypeError:
#     print("Invalid Input")

import csv

file_path = "D:/Test/Emp.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row[0])
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except TypeError:
    print("Invalid Input")