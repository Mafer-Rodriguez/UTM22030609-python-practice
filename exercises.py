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






#tuple
print("Veterinary 'Red dogs'")
print("Tuple of adopted animals")
animal = ("Dog: Leonel", "Cat: Blue", "Mouse: Oscar", "Snake: Nicolas", "Horse: Betty")#this is a tuple
ani = 0
#What it will do with the while loop is that with the len function it counts the elements of the list, 
#for which the variable ani will increase by 1 each time it turns and it will also compare it.
while ani < len(animal):
    print(animal[ani])
    ani+=1
print("These are the adopted animals")



#Dictionary 
print ("Private data of veterinarians.")
privateDatos ={'Name':'Isaac','Age':'32','University':'UAA','Tuition':'22030609'}#this is a dictionary
#In a dictionary you can add and modify the elements
privateDatos['Age']="33"#in this case the age of the veterinarian is being modified or changed.
print (privateDatos)
print("These data are confidential. DO NOT SHARE THEM WITH ANYONE.")



operation = str(input("Enter the basic operation you wish to perform :  "))
#asks the user to enter what basic operation it requires.
firstNumber = int(input("Enter first number: "))
#prompts the user for two numbers.
secondNumber = int(input("Enter second number: "))
#starts an if loop, which compares the operation variable until it is true, if it is true, the suient is executed.
if operation == 'sum':
    result= firstNumber+secondNumber
    print("The result of ",operation,result)
elif operation == 'subtraction':
        result=firstNumber-secondNumber
        print("The result of ",operation,result)
elif operation== 'multiplication':
    result=firstNumber*secondNumber
    print ("The result of ",operation,result)
elif operation=='division':
    result=firstNumber/secondNumber
    print("The result of ",operation,result)
    
else :
    print("operation not found.")
    


