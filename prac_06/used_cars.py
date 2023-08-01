"""
CP1404/CP5632 Practical - 6
Client code to use the Car class.

"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Z350", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Car has fuel: {limo.fuel}")
    limo.drive(115)
    print(f"limo has odometer: {limo.odometer}")
    print(limo)


main()