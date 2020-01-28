                              # Python progam to iterate over 2 lists
                              #PESUDOCODE
                           # Step 1 : declare list1 and list2 as type list
                           # Step 2 : input number of elements in list1
                           # Step 3 : input elements into list1 using for loop
                           # Step 4 ; input number of elements in list2
                           # Step 5 : input elements into list2 using for loop
                           # Step 6 : using for loop with zip function iterate over values in list1 and list 2
                           # Step 7 : print lists in iteration

import itertools

list1 = []
list2 = []
print("enter the number of elements in list1")
number1 = int(input())
for index in range(0,number1) :
   list1.append(input("enter the element"))

print("enter the number of elements in list2")
number2 = int(input())
for index in range(0,number2) :
    list2.append(input("enter the element"))

for (a, b) in zip(list1,list2):
	print (a, b)

