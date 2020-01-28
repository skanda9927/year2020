# Python program to printing the prime numbers within the range of numbers
                                        #PSEUDOCODE
             # Step 1 : Input the range of numbers between which the prime number has to be found out
             # Step 2 : Check if the each number given in range  is divisible by 2 till the input number using mod function
#            # Step 3 : If the modulus function does not returns zero then output the number is
#                                         #a prime number
#            # Step 4 : Repeat step 2 and step 3 till every number is checked in given range


print("Enter the 2 range of numbers to find prime numbers between the range \n please give range in ascending order\n")
print("Enter the first number\n")
range1 = int(input())
print("Enter the second number\n")
range2 = int(input())
number = range1
index = range1
flag = 0
nflag = 0
for index in range (range1,range2) :
    if index > 1 :
        for index1 in range(2, index):
            if (index % index1) == 0 :
              break

            else:
                print(index, "is a prime number")
                flag = flag + 1
                break
if flag == 0 :
    print("prime numbers between",range1,"and",range2,"does not exist" )