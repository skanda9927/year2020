#13. Find factorial of a given number 1) Normal 2) Recursion
                                #PSEUDOCODE
                      #Step 1 : Input the number to find factorial
                      #Step 2 : Enter the type how to find factorial i.e normal method or by recursion
                      #Step 3 : For normal method use built in function to find factorial
                      #Step 4 : For recursion call recursion method
                      #Step 5 : Print factorial of number





def factorial(number):
    if (number == 1 or number == 0) :
        return 1
    else :
        return (number * factorial(number - 1))

number = int(input("Enter the number whose factorial has to be found "))
choice = int (input("enter 1 to find factorial using methods \n enter 2 to find factorial using recursion"))
if choice == 1 :
    print("factorial of given number is ",factorial(number))
elif choice == 2 :
    print("Factorial of", number, "is",factorial(number))
else :
    print("INVALID CHOICE")


