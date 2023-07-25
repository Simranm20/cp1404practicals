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


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
