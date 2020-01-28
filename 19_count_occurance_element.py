                    #19. Python program to Count occurrences of an element in a list
                    #PSEUDOCODE
                    #Step 1: input the total number of elements which needs to be inserted into list
                    #Step 2 : using append  function in for loop enter the elements into the list
                    #Step 3 : input and store the element in element whose occurance has to be found
                    #Step 4 : using count  built in function find occurance of elements and store it in variable named frequency
                    #Step 5 : print the occurance of element


list = []
print("Enter the number of elements you want to insert into List")
number = int(input())

for index in range(0, number):  # index is variable used for looping
    print("enter the number")
    list.append(int(input()))


print("Enter the the element whose number of occurance has to be found ")
element = int(input())
frequency = list.count(element)
print("the number occurance of ", element, "is", frequency)
