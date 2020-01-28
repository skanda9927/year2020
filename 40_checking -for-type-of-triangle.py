#
#checking for type of triangle
#
print("enter the length of hypotenuse of triangle") ;
hypotenuse = int(input());

print("the length of base of triangle");
base = int(input());

print("the length of height of triangle");
height = int(input());

if height == base :
    print("its a isoceles triangle") ;

elif hypotenuse*hypotenuse == ((base*base) +(height*height)) :
    print("its a right angle triangle") ;
    
else :
     print("its scalene triangle")