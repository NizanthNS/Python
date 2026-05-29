# Python file detection

import os

# file_path = "test.txt"
#
# if os.path.exists(file_path):
#     print(f"The location {file_path} Exists")
# else:
#     print(f"That location does not exist")

file_path = "D:/Data Analyst/SQL.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} Exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print(f"That location does not exist")