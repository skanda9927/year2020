#48. Write a Python program to list all files in a directory in Python
                #PSEUDOCODE
            #Step 1 : Input enter the absolute path of directory to list all files into path variable
            #Step 2 : Store details of files in a list named file_list using built in method listdir
            #Step 3 : Print all files and sub directories details stored in file_list


import os
path = input("enter the absolute path of directory to list all files")
file_list = os.listdir(path)
print(file_list)