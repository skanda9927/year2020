#
#8. Sum of an array of numbers
#
#PSEUDOCODE
#
#1: input total number of numbers in array
#2: create and initialise variable sum_of_array to zero
#3: take input of numbers one by one and store it in array number_list and update sum_of_array by adding inputed element to it using a for loop
#4: print the sum_of_array






import array 
   
number_list = array.array('I', [ ])  
sum_of_array = 0
print ("enter the total number of numbers in a array")
number = int (input())
for index in range (0 ,number ):
        print ("enter the number",index+1)
        number_list.insert(index,int(input()));#index variable to point subjects in number_list array 
        sum_of_array = sum_of_array + number_list[index]
print("sum of array of given numbers is",sum_of_array)
