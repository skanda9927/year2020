#
#printing multiplication table
#
print("enter the number whose multiplication table has to be genrated \n");
number = int (input());
print("enter the multiplier till which multiplication table has to end\n") ;
multiplier = int (input());
for i in range(1,multiplier+1) : #loop to genrate the multiplication table
    print(number,"*",i,"=",i*number) ;
    