"""
CP1404/CP5632 Practical - 6
Guitar class
"""

from datetime import datetime


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : $(Self.cost:,.2f)"

    def get_age(self):
        now = datetime.now()
        now = now.year
        return self.year - now

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, guitar2):
        return self.year < guitar2.year