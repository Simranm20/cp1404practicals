"""
CP1404/CP5632 Practical 05
Email to name dictionary
"""
data = {}
user_email = None

while user_email != "":
    user_email = input("Email: ")
    temp = user_email.split('@')[0]
    temp2 = temp.split('.')
    name = " ".join(temp2).title()
    data[user_email] = name

    flag = str(input(f"Is your name {name}? (Y/N)"))
    if flag.upper() != "Y" and user_email != "":
        name = input("Name: ")
        data[user_email] = name

for email, name in data.items():
    print(f"{name} ({email})")