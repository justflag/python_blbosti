#Python writing files (.txt, .json, .csv)
import json
import csv

txt_data = "I like Python"

file_path = "output.csv" #relative or absolute

employees = ["John", "Matthew", "Jonah"]

employee = {
    "name": "John",
    "age": 30,
    "job": "none"
}

employees_2d = [["Name", "Age", "Job"],
                ["John", 30, "none"],
                ["Matthew", 25, "programmer"],
                ["Jonah",27,"hitman"]]

with open(file_path, "w") as file: 
    #statement, good practice to close files, returns file object, 
    # "w" is write mode,
    # "x" writes only if it doesnt exist, 
    # "a" for append, 
    # "r" for reading 
    #can be keyword arguments (file=file_path, mode="w")
    # 'file'is file object
    file.write(txt_data)
    print(f"Text file '{file_path}' was created.")

try:
    with open(file_path, "x") as file: 
        file.write(txt_data)
        print(f"Text file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")

with open(file_path, "a") as file: #append data
    file.write("\n" + txt_data)
    print(f"Text file '{file_path}' was created.")

#with open(file_path, "w") as file: #append data
#    for employee in employees:
#        file.write(employee + "\n")
    #file.write(employees) #throws a type error, cant iterate a list directly, needs a loops
#    print(f"Text file '{file_path}' was created.")

#json is made of keyvalue pairs

try:
    with open(file_path, "w") as file: 
        json.dump(employee, file, indent=4)
        print(f"Json file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")

try:
    with open(file_path, "w", newline="") as file: 
        writer = csv.writer(file) #needs to iterate, must use loop, otherwise empty
        for row in employees_2d:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")