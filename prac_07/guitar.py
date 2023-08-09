"""
CP1404/CP5632 Practical - 07
Guitars code
"""


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    # copy the idea from programming language

    def __str__(self):
        """Return string representation of a guitar."""
        return f"{self.name}, Made in {self.year}, ${self.cost}"

    def __lt__(self, other):
        """sort guitar by year"""
        return self.year < other.year
