#
#18.program to interchange the first and last elements in the list
#
#            PSEUDOCODE
#1: Specify that we are using list type
#2: Enter the number of elements you want to insert into the list
#3: Using for loop and append built in function insert the numbers into the list
#4: Using temporary variable swap first and last element of the List
#5: Print all the elements of List  


list = [] 
print ("Enter the number of elements you want to insert into List")
n = int(input())
 
for index in range( 0,n) : #index is variable used for looping
    print("enter the number")
    list.append(int(input()))
   
temporary_variable = list[0]
list[0] = list[n-1]
list[n-1] = temporary_variable 
print("First and Last element swapped list is")
for index in range( 0,n) :
    print(list[index])