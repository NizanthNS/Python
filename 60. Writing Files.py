# Python writing files (.txt, .json, .csv)

# txt_data = "I Like Nothing, You idiot"

# file_path = "output.txt"
# file_path = "D:/Test/output.txt"
#
# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt_file '{file_path}' was created")
# except FileExistsError:
#     print(f"txt_file '{file_path}' already exists")

# employees = ["Alone", "Nothing", "loner", "Broken"]
#
# file_path = "D:/Test/Emp.txt"
#
# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt_file '{file_path}' was created")
# except FileExistsError:
#     print(f"txt_file '{file_path}' already exists")

# import json
#
# employee = {
#     "Name" : "Alone",
#     "Age" : "Nothing",
#     "Job" : "Broken"
# }
#
# file_path = "D:/Test/Emp.json"
#
# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent = 4)
#         print(f"Json_file '{file_path}' was created")
# except FileExistsError:
#     print(f"The Json file already exists")


import json
import csv

employees = [["Name", "Age", "Job"],
            ["Shane", 21, "Bachelor"],
            ["Genos", 35, "Cyborg"],
            ["Saitama", 40, "University"],
            ["Bachelor", 30, "Master"]]

file_path = "D:/Test/Emp.csv"

try:
    with open(file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"CSV_file '{file_path}' was created")
except FileExistsError:
    print(f"The file already exists")