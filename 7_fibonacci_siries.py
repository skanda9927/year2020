#
# FIBONACCI SERIES
#
print ("enter the number of numbers which should be printed in fibonacci series\n")
number = int( input() )
i=0
fnumber=0;
f1number=0;
f2number =1;
if number == 0  :
        print("fibonacci series number is 0")

else :
        for i in range(i,number) : 
            print(fnumber,"\n") ;
            f1number=f2number ;
            f2number=fnumber ;
            fnumber = f1number+f2number ;