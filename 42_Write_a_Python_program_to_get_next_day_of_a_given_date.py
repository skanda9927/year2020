#
# 42: program to find next date
#

#        PSEUDOCODE
#1: Import datetime package since we are using inbuilt date time functions
#2: Take day,month and year as inputs
#3: use timedelta function to increment days by 1 and store it in next_day variable
#4: use string format time function to print date in Indian date format


import datetime
day = int (input("enter the day"))
month = int (input("enter the month"))
year = int (input("enter the year"))

date = datetime.date(year, month , day)
print("given day is",date.strftime("%d/%m/%Y"))

next_day = d + datetime.timedelta(days=1)
print("the next day date is ",next_day.strftime("%d/%m/%Y"))
      