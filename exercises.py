#displays a list of students enrolled in the course.
print ("List")
print("Students enrolled in the course:")
students = ["Emiliano Sams","Carlos Lopez", "Rodrigo Quevedo", "Yuliana Martínez","Isaac Rodriguez", "Maribel Macias "]#this is a list
print (students)
yes= (input("Would you like to add a student?  "))#If the answer is yes, it asks you for the name of the student to enter.
if yes == 'yes':
    students.append(input("Enter the student's name: "))#al nombre que de el usuario, lo une a la lista or adds(append)
    print("Updated list: ")
    for i in students:#displays the list using a for loop, the loop terminates when the list elements are finished.
        print(i)
else: 
    print ("The list has not been modified.")
    
