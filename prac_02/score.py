"""
CP1404/CP5632 - Practical 1
Broken program to determine score status
"""

# TODO: Fix this!

import random


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    score = random.randint(0, 100)
    print("Random score:", score, get_result(score))


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
