                    #37. Write a Python program to count the number of lines in a text file
                                   # PSEUDOCODE
                        #Step 1 : Input absolute path name of the File , store it in variable File_name
                        #Step 2 : Open file in read mode , f is the pointer to file
                        #Step 3 : Count the number of lines using for loop
                        #Step 4 : print Number_of_lines


file_name = input("Enter file name: ")
number_of_lines = 0
with open(file_name, 'r') as f:
    for line in f:
        number_of_lines += 1
print("Number of lines:")
print(number_of_lines)