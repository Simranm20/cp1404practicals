"""
CP1404/CP5632 - Practical 1
Broken program to determine score status
"""

# TODO: Fix this!

import random


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    print("Random score:", get_result(random.randint(0, 100)))


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
