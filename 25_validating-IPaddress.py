#
# checking for valid IP ADDRESS
#
import re #Using buit_in LIBRARY function

print ("Enter the Ip Address in \nXXX.XXX.XXX.XXX format \nXXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX format\n");

ip_address = input();

pattern1 = re.compile("[0-2][0-5][0-6]\.[0-2][0-5][0-6]\.[0-2][0-5][0-6]\.[0-2][0-5][0-6]");# pattern1 stores pattern of RE to check for valid ipv4 address

test = pattern1.match(ip_address);#using built in function match given string to IPv4 address format

# pattern2 stores pattern of RE to check for valid ipv6 address

pattern2 = re.compile("[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]")

test1 = pattern2.match(ip_address)#using built in function match given string to IPv6 address format
if test:
        print ("Acceptable ipv4 address")

elif test1:
        print ("Acceptable ipv6 address")
else:
        print ("Unacceptable ip address")
 