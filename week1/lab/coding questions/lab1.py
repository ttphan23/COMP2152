#Sample Coding Questions 01 Week 01
#Thinh Phan

#Defining Array Variables
array_variable = [1, 4, 7, 9]

#Order of Operations
a = 1
b = 2
c = 3
d = 4
#Not Fully Bracketed Version: e = a - b ** c // d + a % c
#Fully Bracketed Version
e = ((a - ((b ** c) // d)) + (a % c))

#Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

#Common Functions
userAge = int(input("Enter age: "))
userAge += 22
print(f"Now showing the shop items filtered by age: {userAge}")
