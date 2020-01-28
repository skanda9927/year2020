#
#31.Find the character is alphabet or number or special character 
#
#        PSEUDOCODE
#1: Enter the character and store it in a variable called character
#2: Check the character if it is a alphabet or a number using built in function isalpha and isnumeric function 
#3: If the above condition is TRUE print Inputed character is a alphabet or a number 
#4: Else print it is a special character



print("enter the character")
character = input()

if character.isalpha( ) :
     print("Inputed character is alphabet")

elif character.isnumeric( ) :
    print("Inputed character is a number ") 

else : print("Inputed character is a special character")   