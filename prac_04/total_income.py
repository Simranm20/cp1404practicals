"""
CP1404/CP5632 Practical 04
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}:"))
        # income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        # print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
        print(f'Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}')


main()
