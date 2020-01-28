#16. Environment variables in python: Print all key, values from environment.
# Check if a variable TEXT_DATA is set in environment, if so print its value.
                      #  PSEUDOCODE
                #Step 1 : retrieve environment variables and store it in environment_variables
                #Step 2 : print retrieve environment variables and store it in environment_variables
                #step 3 : try printing the environment variable TEXT_DATA ,if not set it gives error
                #Step 4 : Set environment variable TEXT_DATA with value
                #Step 5 : print newly set environment variable



# importing os module
import os
import pprint

# Get the list of user's
# environment variables
environment_variables = os.environ

# Print the list of user's
# environment variables
print("User's Environment variable:")
pprint.pprint(dict(environment_variables), width = 1)

# checking for environment variable named TEXT_DATA and setting TEXT_DATA if not configured
try:
    print("TEXT_DATA", os.environ['TEXT_DATA'])
except KeyError:
    os.environ['TEXT_DATA'] = 'www.cliqrtech.com'
    print("new env variable configured")
    print("TEXT_DATA", os.environ['TEXT_DATA'])