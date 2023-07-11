"""
CP1404/CP5632 - Practical 2
Pseudocode for Main menu following the standard structure
that uses a main and other functions.menu
"""


def get_valid_score():
    """Function to get a valid score from the user"""
    score = -1
    while score < 0 or score > 100:
        score = int(input("Enter a valid score (0-100 inclusive): "))
        if not (0 < score > 100):
            print("Invalid score. Please try again.")
    return score


def print_result(score):
    """Function to determine and print the result based on the score"""
    if score >= 70:
        print("Pass")
    else:
        print("Fail")


def show_stars(score):
    """Function to show stars based on the score"""
    print("*" * score)


def main():
    """Main function to run the program"""
    option = ""

    while option != "Q":

        print("\nMAIN MENU")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        option = input("Select an option: ").upper()

        if option == "G":
            score = get_valid_score()
        elif option == "P":
            print_result(score)
        elif option == "S":
            show_stars(score)
        elif option == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid option. Please try again.")


# Run the main function to start the program
if __name__ == "__main__":
    main()
