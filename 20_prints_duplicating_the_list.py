            #20. Python Program to print duplicates from a list of integers
            #                        PSEUDOCODE
            # Step 1 : input the number of elements you want to insert into list
            # Step 2 : using for loop with append funtion enter the elements into the list
            # Step 3 : copy the elements of the list to duplicate_list using append function
            # Step 4 : print the elements of duplicated list

list = []
duplicate_list = []
print ("Enter the number of elements you want to insert into List")
number = int(input())

for index in range( 0,number) : #index is variable used for looping
    print("enter the number")
    list.append(int(input()))


for index in range( 0,number) :

    duplicate_list.append(list[index])

for index in range( 0,number) :
    print(duplicate_list[index])
print("duplicated list successfully")