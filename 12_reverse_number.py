                    #12. Python program to extract and print digits in reverse order of a number
                    #PSEUDOCODE
       # Step 1 : input the number and store it into the variable number
       # Step 2 : create the variable named reverse_number and initialise it to zero
       # Step 3 : using while loop extract the digits using mod function
       # Step 4 : print the reverse_number
print ("enter the number")
number = int(input())
reverse_number = 0
  
while(number > 0): 
    remainder = number%10
    reverse_number = reverse_number*10 + remainder
    number = number//10
      
print("Reverse of the number is ",reverse_number) 

    
    
 
