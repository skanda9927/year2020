#
# floyds triangle
#
# PSEUDOCODE
#1: Input the range  i.e number of rows till which Floyds triangle has to be printed
#2: Nesting for loop to print floyds triangle and printing the row elements

size = int(input("Enter the number of rows till which floyds triangle has to be printed: \t "))
 
print("\nFLOYD'S TRIANGLE with numbers: \n")
number = 1
 
# 2 for loops, one for column looping another for row looping
# i loop for column looping and j loop for row looping
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number = number + 1
    print()
print("\n")

