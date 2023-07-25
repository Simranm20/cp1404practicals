"""CP1404/CP5632 Practical - 6
Car class
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel  # instant variable
        # self._odometer = 0 # _name means hiding it
        self.odometer = 0

