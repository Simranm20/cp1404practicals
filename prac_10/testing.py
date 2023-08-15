import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)  # TODO 1: Fixed repeat_string function using join()


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # TODO 4: Change condition to >= to fix the function


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('this is another test')
    'This is another test.'
    """
    formatted_sentence = phrase.capitalize()  # Capitalize the phrase
    if not formatted_sentence.endswith('.'):
        formatted_sentence += '.'  # Add a full stop if not already present
    return formatted_sentence


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # TODO 2: Write assert statements to test if Car sets the fuel correctly
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"


run_tests()

# TODO 3: Uncomment the following line and run the doctests
doctest.testmod()

# TODO 5: Write and test a function to format a phrase as a sentence
# This is already done in the code above.
