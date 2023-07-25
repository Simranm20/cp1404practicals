"""
CP1404/CP5632 Practical - 6
Programming Language class with tests.
"""


class ProgrammingLanguage:
    def __init__(self, name='Python', typing='Dynamic', reflection=True, year=1991):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def __str__(self):
        return f'{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}'

