"""
CP1404/CP5632 Practical 05
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)
print(CODE_TO_NAME["QLD"])
print(CODE_TO_NAME["VIC"])
state_code = input("Enter short state(hit enter to quit): ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:  # find key
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state (hit enter to quit): ").upper()
print("Bye.")
for state_code in CODE_TO_NAME:
    print(f"{state_code:3} is {CODE_TO_NAME[state_code]} ")
