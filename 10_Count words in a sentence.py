                            #10. Count words in a sentence
                            #PESUDOCODE
                    #Step 1 : input the sentence and store it into the variable test_string
                    #Step 2 : print the  original string
                    #Step 3 : using len function to count the number of words along with split function
                    #Step 4 : print number of words stored in variable word_count

# initializing string 
print("Enter the sentence for words to be counted\n")
test_string = input( )

# printing original string 
print ("The original string is : " + test_string) 

# using split() 
# to count words in string 
word_count = len(test_string.split())
print(word_count )
# printing result 
print ("The number of words in string are : ",word_count )
