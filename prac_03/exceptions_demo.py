"""
CP1404/CP5632 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
#A ValueError will occur if the user enters a value that cannot be converted to an integer. 
if the user enters a floating-point number, the int() function will raise a 
ValueError when attempting to convert the input to an integer.
2. When will a ZeroDivisionError occur?
#A ZeroDivisionError will occur if the user enters a denominator of zero. 
Division by zero is mathematically undefined, so attempting to perform such division 
will raise a ZeroDivisionError.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#Yes, we can modify the code to avoid the possibility of a ZeroDivisionError.
 We can include a check before performing the division to ensure that the denominator is not zero. 
"""

