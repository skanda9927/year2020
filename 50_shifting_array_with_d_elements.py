                            #50. Python program to rotate an array by 'd' elements
                            #PSEUDOCODE
                   # Step 1 : Input total number of numbers
                   # Step 2 : Input number of elements the array has to be rotated
                   # Step 3 : Input elements into array
                   # Step 4 : Using for loop ,rotate elements depending upon number of elements
                   # Step 5 : Print rotated array



import array

sequence_of_numbers_list = array.array('I', [])

print("enter the total number of numbers ")
total_number_of_numbers = int(input())
shift= int(input("enter the number of elements the array has to be rotated"))


for index in range(0, total_number_of_numbers):  # index variable to point subjects in NUMBER LIST array
    print("Enter the element of array")
    sequence_of_numbers_list.insert(index, int(input()))

for shift1 in range(0,shift) :
    for index in range(0, total_number_of_numbers):
        if index == 0 :
            temp = sequence_of_numbers_list[index]
        if index < (total_number_of_numbers-1) :
            sequence_of_numbers_list[index] =sequence_of_numbers_list[index+1]
        if index == total_number_of_numbers-1 :
            sequence_of_numbers_list[index] = temp

for index in range(0, total_number_of_numbers):
    print(sequence_of_numbers_list[index])




#print("Maximum number is ", maximum_number)