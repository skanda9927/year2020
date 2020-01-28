#
#31.Find the character is UPPERCASE or LOWERCASE alphabet  character 
#
#        PSEUDOCODE
#1: Enter the character and store it in a variable called character
#2: Check the character if it is a UPPERCASE alphabet or LOWERCASE alphabet using built in function isupper and islower function 
#3: If the above condition is TRUE print Inputed character is a UPPERCASE or LOWERCASE alphabet 



print("enter the character")
character = input()

if character.isupper() :
     print("Inputed character is UPPERCASE alphabet")

elif character.islower( ) :
    print("Inputed character is a LOWERCASE alphabet ") 

else : print("Inputed character is not a alphabet ")   