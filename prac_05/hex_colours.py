"""
CP1404/CP5632 Practical 05
Hexadecimal colour lookup
"""
COLOR_NAME_TO_COLOR_CODE = {
    "aliceblue": "#f0f8ff",
    "aqua": "#00ffff",
    "bittersweet shimmer": "#bf4f51",
    "brick red": "#cb4154",
    "bright lilac": "#d891ef",
    "candy pink": "#e4717a",
    "baby pink": "#f4c2c2",
    "cerise": "#de3163",
    "daffodil": "#ffff31",
    "deeppink1": "#ff1493"
}

color_name = input("Enter color name (hit enter to quit): ").lower()
while color_name != "":
    if color_name in COLOR_NAME_TO_COLOR_CODE:  # find key
        print(f"{color_name} is {COLOR_NAME_TO_COLOR_CODE[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name (hit enter to quit): ").lower()
print("Bye.")