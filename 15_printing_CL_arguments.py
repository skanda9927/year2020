                    #15.Common line arguments to python: Print count, list them, print the last argument value
                                #PSEUDOCODE
                       # Step 1 : import the module named sys
                       # Step 2 : copy the variables stored in the system built in list argv
                       # Step 3 : find the length  of argument_list using len function and store it nin variable length
                       # Step 4 : using for loop with length print all values stored in argument_list
import sys

# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv
length = len(argumentList)
for index in range(0,length) :
    print (argumentList[index])
