#36. Write a python program to find the longest word in given paragraph
                        #PSEUDOCODE
                    #Step 1 : Input paragraph as a string
                    #Step 2 : split input into small strings of words







longest_word = []
print("enter the praragraph")
string = input()
length = 0
word = string.split()
print (word)

for word in string.split(): # Finding longest word in sentence
    if (len(word) > length):
       length = len(word)
print (word)

for index in range(0,len(word)) :
    if (len(word) > length): longest_word = longest_word + join(word)
print("longest word is ",word,"longestWordLength",length)

