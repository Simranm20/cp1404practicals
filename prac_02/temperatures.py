"""
CP1404/CP5632 - Practical 2
Pseudocode for temperature conversion
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")

    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
