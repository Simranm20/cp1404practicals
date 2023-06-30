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

