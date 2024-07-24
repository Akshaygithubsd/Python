# import os

# def print_directory_contents(path):
#     try:
#         with os.scandir(path) as entries:
#             for entry in entries:
#                 print(entry.name)
#     except FileNotFoundError:
#         print(f"The directory {path} does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access {path}.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# directory_path = '/'  # You can change this to any directory path
# print_directory_contents(directory_path)



#more easy code
import os

#specify the directories you want to list
directory_path="/"
#List all files and directories in specified path using os module
contents=os.listdir(directory_path)
#print each file and directory name 
for i in contents:
    print(i)
