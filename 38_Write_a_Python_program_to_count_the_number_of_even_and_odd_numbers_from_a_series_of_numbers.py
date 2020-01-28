#
# 38. Write a Python program to count the number of even and odd numbers from a series of numbers.
#
#PSEUDOCODE
#1:take input total number of numbers in which number of odd or even numbers has tobe calculated
#2:initialise even and odd number count to zero
#3: input the sequence of numbers
#4: using modulus functiion check the number modulus 2 is equal to zero for each number
#5:if number modulus 2 is equal to zero increment even number count with 1 else increment odd number count with 1
#6:print the even and odd number count 

import array 
   
number_list = array.array('I', [ ])  
even_number_count = 0 
odd_number_count =0
print ("enter the number of numbers in which number of odd or even number has to known") 
total_number_of_numbers = int(input()); 

for index in range (0, total_number_of_numbers):
        print("enter the number") #index variable to point subjects in number_list array
        number_list.insert(index,int(input())); 
  
for index in range (0, total_number_of_numbers):
    if ((number_list[index])%2) == 0 :
        even_number_count = even_number_count + 1
    else : odd_number_count = odd_number_count + 1
    
print("total number of even number is ",even_number_count,"total number of odd number count is",odd_number_count)