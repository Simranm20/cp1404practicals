"""
CP1404/CP5632 - Practical 3
Quick file opening/writing/reading exercises
"""

# Program 1
name = input("Enter your name: ")

# Opening the file in write mode and writing the name to it
with open("name.txt", 'w') as file:
    file.write(name)

# Program 2
# Opening the file in read mode and reading the name from it
with open("name.txt", 'r') as file:
    name = file.read()
print("Your name is", name)

# Program 3
# Opening the file in read mode and reading the numbers
with open("numbers.txt", 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())

# Adding the numbers and printing the result
result = number1 + number2
print("The result is", result)

# Program 4
# Opening the file in read mode and reading all lines
with open("numbers.txt", 'r') as file:
    lines = file.readlines()

# Initializing the total sum
total = 0

# Iterating over each line and adding the numbers to the total
for line in lines:
    number = int(line)
    total += number

# Printing the total sum
print("The total is", total)
