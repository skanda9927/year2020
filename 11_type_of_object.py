list = [] 
print ("Enter the number of elements you want to insert into List")
n = int(input())
 
for index in range( 0,n) : #index is variable used for looping
    print("enter the number")
    list.append(int(input()))
    
l = len(list)
print("last element removed in list is ",list[l-1])
#n1 = list[l]
list.pop(l-1)

for index in range( 0,l-1) : 
 print(list[index])   