                                #  Python program calculate simple interest
                                            #PSEUDOCODE
                                # Step 1 : Input the principal amount
                                # Step 2 : Input the duration for which simple interest has to be calculated in years
                                # Step 3 : Input the rate  of interest per annum
                                # Step 4 : Calculate the simple interest using the formula
                                           # simple_interest =principle_amount*time*rate_of_interest/100
                                # Step 5 : Print the simple_interest


print ("\n enter the principle amt \n ")
principle_amount = int(input ())
print ('enter the duration for which simple interest has to be calculated in years \n')
time = int (input())
print ('enter the rate  of interest per annum\n')
rate_of_interest = int ( input())
simple_interest  = principle_amount*time*rate_of_interest/100
print ('\n simple interest as per given data is ',simple_interest)
