"""
CP1404/CP5632 Practical 04
Quick pick program
"""

import random

ARG = [1, 45, 6]

number_of_quick_picks = int(input("How many quick picks? "))
if number_of_quick_picks < 0:
    print("Enter Number Greater than 0")
    number_of_quick_picks = int(input("How many quick picks? "))
else:
    for i in range(number_of_quick_picks):
        quick_pick = []

