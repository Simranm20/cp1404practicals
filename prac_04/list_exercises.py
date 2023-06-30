"""
CP1404/CP5632 Practical 04
List exercises
"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
numbers = []
for i in range(5):
    valid = False
    while not valid:
        try:
            number = int(input("Number: "))
            numbers.append(number)
            valid = True
        except ValueError as e:
            print("Not a number. Please enter a number.")

print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the number is {sum(numbers) / len(numbers):.1f}")


