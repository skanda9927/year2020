# Python code to find the URL from an input string
# Using the regular expression
                                #PSEUDOCODE
                          #  Step 1 : input the string
                          #  Step 2 : use built in method findall to match the pattern for URL store it in urls
                          #  Step 3 : print all URLs
import re # import regular expression module as we are using pattern matching
text = input("enter the string to check presence of URL")
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)
