#2  Program to calculate compund interest
# PSEUDOCODE
# Step 1 : Input the principal amount
# Step 2 : Input the duration for which simple interest has to be calculated in years
# Step 3 : Input the rate  of interest per annum
# Step 4 : Calculate the simple interest using the formula
#compound_interest = principle*((1+rate_of_interest)/100)*time
# Step 5 : Print the simple_interest

print ("\n enter the principle amt \n ")
principle = int(input ())
print ('enter the duration for which compound interest has to be calculated in years \n')
time = int (input())
print ('enter the rate  of interest per annum\n')
rate_of_interest = int ( input())
compound_interest = principle*((1+rate_of_interest)/100)*time
print ('\n compound  interest as per given data is ',compound_interest)