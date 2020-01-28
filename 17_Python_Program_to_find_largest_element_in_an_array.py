#
#49. Write a Python function to find the maximum and minimum numbers from a sequence of numbers
#
#PSEUDOCODE
#1: take input total numbers for which maximum_number  has to be FOUND
#2: Initialise maximum number to zero
#3: create an integer array and  store all the numbers
#4: check each element for condition whether the present pointed number is greater than or lesser than the maximum number 
#5: if the condition holds true for step 4 condition then update maximum  number value


import array 
   
sequence_of_numbers_list = array.array('I', [ ])  
 
print ("enter the number of numbers for which maximum number has to be detected") 
total_number_of_numbers = int(input()); 
maximum_number = 0

for index in range (0, total_number_of_numbers): #index variable to point subjects in NUMBER LIST array
    print("Enter the number")
    sequence_of_numbers_list.insert(index,int(input())); 
    if sequence_of_numbers_list[index] >= maximum_number :
        maximum_number = sequence_of_numbers_list[index]

print("Maximum number is ",maximum_number)