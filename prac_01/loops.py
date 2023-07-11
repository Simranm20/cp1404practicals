"""
CP1404/CP5632 - Practical 1
program that displays all the odd numbers between
1 and 20 with a space between each one
"""
# odd numbers
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# (a) count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# (b) count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# (c) print n stars
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end=' ')
print()

# (d) print n lines of increasing stars
stars = int(input("Number of stars: "))
for i in range(1, stars+1):
    print("*" * i)
print()
