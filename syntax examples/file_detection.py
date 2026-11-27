#Python file detection

import os

file_path = "test_detection.txt" #relative path 
absolute_file_path = "/Users/stepan/Documents/python_blbosti/test_detection.txt" #absolute path

if os.path.exists(file_path): # true or false
    print(f"The location '{file_path}' exists")
    print(f"The absolute path is '{absolute_file_path}'")

    if os.path.isfile(file_path): #checks if target is a file
        print("That is a file.")
    elif os.path.isdir(file_path): #checks if target is a directory
        print("This is a directory.")
else:
    print("That location doesn't exist.")
