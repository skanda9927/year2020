# Python program to check whether number is prime or not
                                # PSEUDOCODE
                        # Step 1 : Input the number to be checked for prime number
                        # Step 2 : Check if the number is divisible by 2 till the input number using mod function
                        # Step 3 : If the modulus function returns zero then output the number is
                                        #not a prime number
                                   # Else print the number is prime number




number = int(input("Enter any number: "))

if number > 1 :
    for index in range(2, number):
        if (number % index) == 0 :
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")
            break

