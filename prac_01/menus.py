"""
CP1404/CP5632 - Practical 1
program to create a very simple menu-driven program
"""
name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input("Enter chocie: ")
while choice != "Q":
    if choice == "H" or choice == "h":
        print("Hello", name)
        print()
    elif choice == "G" or choice == "g":
        print("Goodbye", name)
        print()
    else:
        print("Invalid choice")
        print()
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input("Enter choice: ")
print()
print("Finished- Bye!")
