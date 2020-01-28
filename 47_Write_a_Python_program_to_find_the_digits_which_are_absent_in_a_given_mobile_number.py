#
#47. Write a Python program to find the digits which are absent in a given mobile number
#
#PSEUDOCODE
#1: input mobile number digits one by one and store it in a array
#2: create and inititalise the count as zero for all digits individually
#3: check each digit occurance in given mobile number if found increment the count of digit by 1
#4: if count of digit is zero print it as a missing digit  

import array 
   
mobile_number = array.array('I', [ ])  
one_number_count = 0 
two_number_count = 0
three_number_count = 0
four_number_count = 0
five_number_count = 0
six_number_count = 0
seven_number_count = 0
eight_number_count = 0
nine_number_count = 0
zero_number_count = 0

print ("enter the ten digit mobile number") 
for index in range (0 ,10 ):
        print("enter the digit ",index+1)
        mobile_number.insert(index,int(input()));#index variable to point subjects in mobile_number array 
for index in range (0 ,10 ):
    if mobile_number[index] == 1 :
        one_number_count = one_number_count + 1
    elif mobile_number[index] == 2 :
        two_number_count = two_number_count + 1
    elif mobile_number[index] == 3 :
        three_number_count = three_number_count + 1
    elif mobile_number[index] == 4 :
        four_number_count = four_number_count + 1
    elif mobile_number[index] == 5 :
        five_number_count = five_number_count + 1
    elif mobile_number[index] == 6 :
        six_number_count = six_number_count + 1
    elif mobile_number[index] == 7 :
        seven_number_count = seven_number_count + 1
    elif mobile_number[index] == 8 :
         eight_number_count = eight_number_count + 1
    elif mobile_number[index] == 9 :
        nine_number_count = nine_number_count + 1
    elif mobile_number[index] == 0 :
        zero_number_count = zero_number_count + 1
       
if one_number_count == 0 :
    print("missing digit is 1")
if  two_number_count == 0 :
    print("missing digit is 2") 
if  three_number_count == 0 :
    print("missing digit is 3") 
if  four_number_count == 0 :
    print("missing digit is 4") 
if  five_number_count == 0 :
    print("missing digit is 5") 
if  six_number_count == 0 :
    print("missing digit is 6") 
if  seven_number_count == 0 :
    print("missing digit is 7") 
if  eight_number_count == 0 :
    print("missing digit is 8")
if  nine_number_count == 0 :
    print("missing digit is 9")
if  zero_number_count == 0 :
    print("missing digit is 0")
     