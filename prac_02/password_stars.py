"""
CP1404/CP5632 - Practical 2
Password check with functions
"""


# imports

# CONSTANTS

def main():
    """Function docstring"""
    # get password
    password = get_password()
    print(password)


def get_password():
    """Function docstring"""
    # statements...
    password = input('Enter password: ')
    for _ in password:
        print('*', end="")
    print()

    # another way
    print('*' * len(password))
    return password


# Call the main function to run the program
main()
