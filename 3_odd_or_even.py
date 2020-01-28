#3 : Python program to find number is  odd or even
        #PSEUDOCODE
        #step1:create a variable number and enter the number
        #step2:check if the given number is divisible by 2 and remainder equal to 0 using mod function
        #step3:if step 2 is true print its a even
        #step4:else print number inputed is odd




print ("\n enter the number")
number = int(input ())
if number%2 == 0:
    print('\n',number,'the number inputed is even')
else:
    print('\n number inputed',number,' is odd')
    