"""
CP1404/CP5632 Practical - 6
Basic manual tests for Guitar class
"""
from guitar import Guitar


def test():
    name = input("Enter Name ")
    year = int(input("Enter Year "))
    cost = input("Enter cost ")

    guitar = Guitar(name, year, cost)
    guitar2 = Guitar("Guitar 2 ", 1990, 1000)

    print(f"{guitar.name} get_age() - Expected {0}. Got {guitar.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {0}. Got {guitar2.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {0}. Got {guitar.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {0}. Got {guitar2.is_vintage()}")


if __name__ == '__main__':
    test()