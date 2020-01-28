#
#checking divisibilty by 5 and 11
#
print("enter the number to check for divisibility by 5 and 11")
number=int(input());
flag = 0 ; #variable to keep track of number divisible by 11 or 5 or by both numbers
if number % 5 == 0  :
        flag = 1 ;
if number % 11 == 0  :
    flag = flag +11 ;
if flag == 0 :
    print("Sorry !!number is not divisible by 5 or 11");
elif flag == 1 :
    print ("number divisible by 5") ;
elif flag == 11:
    print ("number divisible by 11") ;
elif flag == 12 :
    print ("number is divisble by 11 and 5")
        