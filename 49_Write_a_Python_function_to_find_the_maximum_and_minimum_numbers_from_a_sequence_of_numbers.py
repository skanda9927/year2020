#
#49. Write a Python function to find the maximum and minimum numbers from a sequence of numbers
#
#PSEUDOCODE
#1: take input total numbers for which maximum_number and minimum_number has to be FOUND
#2: create an integer array to store all the numbers
#3: Initialise maximum number and minimum number to first element of array
#4: check each element for condition whether the present pointed number is greater than or lesser than the maximum number or minimum number respectively
#5: if the condition holds true for step 4 condition then update maximum and minimum number values respectively


import array 
   
sequence_of_numbers_list = array.array('I', [ ])  
 
print ("enter the number of numbers for which maximum  and minimum number has to be detected") 
total_number_of_numbers = int(input()); 

for index in range (0, total_number_of_numbers): #index variable to point subjects in NUMBER LIST array
    print("Enter the number")
    sequence_of_numbers_list.insert(index,int(input())); 

maximum_number = sequence_of_numbers_list[0]
minimum_number = sequence_of_numbers_list[0]

for index in range (0, total_number_of_numbers):
    if sequence_of_numbers_list[index] >= maximum_number :
        maximum_number = sequence_of_numbers_list[index]
    if sequence_of_numbers_list[index] <= minimum_number :
        minimum_number = sequence_of_numbers_list[index]
        
print("Maximum number is ",maximum_number,"Minimum number is ",minimum_number)