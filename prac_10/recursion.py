def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO 1: The output of do_it(5) will be 3.
# TODO 2: Use a debugger to step through and see the actual process.

print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)


# TODO 3: The output of do_something(4) will be a sequence of squared values from 16 to 0.
# TODO 4: Use a debugger to step through and see the actual process.
do_something(4)


# TODO 5: Fix the do_something() function to work according to the docstring.

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return  # Base case to stop recursion
    print(n ** 2)
    do_something(n - 1)


do_something(4)
