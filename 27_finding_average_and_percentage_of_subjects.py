import array 
   
# initializing array with array values 
# initializes array with signed integers 
arr = array.array('I', [ ])  
total = 0 
# printing original array 
print ("enter the number of subjects for which average and percentage has to be calculated") 
n = int(input()); 
for i in range (0, n): 
    #print (arr[i], end=" ") 
# using append() to insert new value at end 
    arr.insert(i,int(input())); 
  
# printing appended array 
#print("The appended array is : ", end="") 
for i in range (0, n): 
    print (arr[i]) 
      
# using insert() to insert value at specific position 
# inserts 5 at 2nd position 
#arr.insert(2, 5) 
  
#print("\r") 
  
# printing array after insertion 
#print ("The array after insertion is : ", end="") 
for i in range (0, n):
    total = total + arr[i]
average = float (total/n)
percentage = float ((total/(n*100))*10)
#for i in range (0, 5): 
 #   print (arr[i], end=" ") 
print("average is",average,"/n percentage is",percentage)
