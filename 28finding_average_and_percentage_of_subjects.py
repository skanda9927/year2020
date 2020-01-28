#
#28. Total average and Percentage of ’N’ Subjects
#pseudocode
#1:asking user to specify number of subjects for which average and percentage has to be calculated(number)
#2:Assuming the maximum marks for each subject is 100 
#3: average formula is summation of marks scored in each subjects (total) divided by number of subjects
#4: percentage formula is summation of marks scored in each subjects (total) divided by 
#number of subjects divided by summation of maximum marks in each subjects  multiplied by 100  
import array 
   
marks_list = array.array('I', [ ])  
total_marks = 0 

print ("enter the number of subjects for which average and percentage has to be calculated") 
number_of_subjects = int(input()); 

print("Enter the marks of each subject")
for index in range (0, number_of_subjects):
        print("enter the marks of subject",index+1) #index variable to point subjects in marks_list array
        marks_list.insert(index,int(input())); 
  
for index in range (0, number_of_subjects):
    total_marks = total_marks + marks_list[index]
average_marks = float (total_marks/number_of_subjects)
percentage = float ((total_marks/(number_of_subjects*100))*100)
print("average is",average,"\n percentage is",percentage)
