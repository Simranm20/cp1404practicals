"""
CP1404/CP5632 Practical 05
Email to name dictionary
Estimate: 30 minutes
Actual:   60 minutes
"""
email_to_name = {}
email_address = input("Email: ")

while email_address != "":
    email_no_at = email_address.split('@')[0]
    email_no_full_stop = email_no_at.split('.')
    name = " ".join(email_no_full_stop).title()
    email_to_name[email_address] = name

    flag = str(input(f"Is your name {name}? (Y/N) "))
    if flag.upper() != "Y" and email_address != "":
        name = input("Name: ")
        email_to_name[email_address] = name
    email_address = input("Email: ")
print(email_to_name)
for email, name in email_to_name.items():
    print(f"{name} ({email})")
