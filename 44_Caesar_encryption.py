                        # 44_PROGRAM FOR CAESAR ENCRYPTION
                        # PESUDOCODE
                 #Step 1 : Input the string
                 #Step 2 : input the value by characters has to be shifted and encrypted
                 #Step 3 : retrieve ASCII value character by character
                 #Step 4 : Shift value by given value
                 #Step 5 : convert ASCII value to character
                 #Step 6 : store encrypted character in string
                 #Step 7 : print encrypted message string



string = input("enter the string")
encrypted_string = ""
shift =int(input("enter the number by which characters has to be shifted and encrypted"))
for index in range(0,len(string)) :
    plain_character = string[index]
    number= ord(plain_character) #retrieving ASCII value of character
    number= number+shift #changing ASCII by shift value
    encrypted_character = chr(number) # converting ASCII value to character
    encrypted_string=encrypted_string + encrypted_character #storing encrypted character in string

print("encrypted string ",encrypted_string)
