"""
CP1404/CP5632 Practical 04
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    list_of_records = []

    input_file = open(FILENAME)



main()
