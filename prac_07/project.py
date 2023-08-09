"""
CP1404/CP5632 Practical - 07
Project code
start time: 11:15 pm
End time: 11:45 pm
"""


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, estimate, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = float(estimate)  # Convert estimate to float
        self.completion = completion

    def __str__(self):
        """Return string representation of a project."""
        return f"{self.name}, start: {self.start_date} , priority {self.priority}, estimate: ${self.estimate:.2f}, " \
               f"completion:  {self.completion} "


def main():
    project = Project('Build Car Park', '12/09/2021', 2, 600000.0, 95)
    print(project)


if __name__ != 'main':
    main()
