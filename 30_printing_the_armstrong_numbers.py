#30. Print first 5 Armstrong number from 100
                            #PSEUDOCODE
                         #Step 1 : Input number of armstrong numbers have to be printed
                         #Step 2 : Extract digits using mod function for each number from 100
                         #Step 3 : Find sum of cube of digits and store it in armstrong_number
                         #Step 4 : check whether sum of cube of digits is equal to number
                         #Step 5 : If the Step 4 condition holds good print armstrong_number
                         #Step 6 : else increment number to be checked by 1





count = int(input("enter the number of armstrong numbers to be genrated from 100"))
count1 = 0
number = 100
while count1 < count :

    number1 = number
    armstrong_number = 0
    while (number1 > 0):
        remainder = number1 % 10
        armstrong_number = armstrong_number+ remainder**3
        number1 = number1 // 10
    if armstrong_number == number :
        print(armstrong_number)
        count1 = count1 + 1
    number = number +1