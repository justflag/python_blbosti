#Python reading files (.txt, .json, .csv)
import json
import csv
file_path_txt = "/Users/stepan/Documents/python_blbosti/output.txt"
file_path_json = "/Users/stepan/Documents/python_blbosti/output.json"
file_path_csv = "/Users/stepan/Documents/python_blbosti/output.csv"

try:
    with open(file_path_txt, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("This file was not found.")
except PermissionError:
    print("You do not have permission to read that file.")

try:
    with open(file_path_json, "r") as file:
        content = json.load(file)
        print(content["job"])
except FileNotFoundError:
    print("This file was not found.")
except PermissionError:
    print("You do not have permission to read that file.")

try:
    with open(file_path_csv, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[1]) #print lines from 0 to n
        print(content)
except FileNotFoundError:
    print("This file was not found.")
except PermissionError:
    print("You do not have permission to read that file.")