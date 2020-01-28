#39. Write a Python program to check the validity of password input by users.
# ( At least 1 letter between [a-z] and 1 letter between [A-Z], At least 1 number between [0-9],
# At least 1 character from [$#@], Minimum length 6 characters, Maximum length 16 characters)
								#PSEUDOCODE
							#Step 1 : Input the  password and store it in variable password
							#Step 2 : Check Minimum length 6 characters, Maximum length 16 characters using len function
							#Step 3 : Search for specified conditions using search method of re
							#Step 4 : If any condition fails set flag to -1
							#Step 5 : print validity status of password using status of flag


import re
password = input("Enter the password to check for validation\n ")
flag = 0

if (len(password)<6 & len(password)>16):
	flag = -1

elif not re.search("[a-z]", password):
	flag = -1

elif not re.search("[A-Z]", password):
	flag = -1

elif not re.search("[0-9]", password):
	flag = -1

elif not re.search("[#@$]", password):
	flag = -1

elif re.search("\s", password):
	flag = -1

else:
	flag = 0
	print("Valid Password")


if flag ==-1:
	print("Not a Valid Password")
