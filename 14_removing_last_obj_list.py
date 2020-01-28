                    #A way to remove the last object from a list

                    #PSEUDOCODE
#Step 1: enter the elements into the list using append function
#STEP 2 : find the length of the list using len function
#Step 3 : using pop function remove last element by pointing the to last element of the array
#step 4: print the updated list
list = []

print ("Enter the number of elements you want to insert into List")
number = int(input())
 
for index in range( 0,number) : #index is variable used for looping
    print("enter the number")
    list.append(int(input()))
    
length = len(list)
print("last element removed in list is ",list[length-1])
list.pop(length-1)
index = 0
for index in range( 0,l-1) : 
 print(list[index])   