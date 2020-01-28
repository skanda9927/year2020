#program to print ten odd or ten even numbers


                #PSEUDOCODE
                #step1:create a varible number and enter the number from that even or odd numbers to be printed
                #step2: input number 1 for odd numbers to be printed \n input number 2 for even numbers to be printed
                        #To print first 10 odd or even numbers
                #Step 3 ; check if the given number is divisible by 2 and remainder equal to 0 using mod function
                #Step 4 : check choice regarding printing list of 10 even or odd
#               #Step 5 : print the list of numbers depending upon choice using for loop



print("enter the integer number from that number odd or even numbers to be printed\n")
number = int(input())
print ("\n press input number 1 for odd numbers to be printed \n input number 2 for even numbers to be printed")

choice = int(input())

if number % 2 == 0 : #checking odd or even numbers
    if choice == 1 :
        number = number+1 ; 
        for index in range(10) :
            print(number)
            number = number+2 ;
    else :  
        for index in range(10) :
            print(number+2)
            number = number+2
         
        
else :        
    if choice == 1 :
         for index in range(10) :
            
            print(number+2)
            number = number+2
        
    else :  
        number = number+1
        for index in range(10) :
            print(number)
            number = number+2
        
        
           
    
    
       
    