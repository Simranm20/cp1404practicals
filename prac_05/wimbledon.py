"""
CP1404/CP5632 Practical 05
Wimbledon data-reading, processing and displaying
Estimate: 60 minutes
Actual: 1 hour
"""
records = []
champion = {}
country = set()
countryNumber = 1
championNumber = 2

with open("wimbledon.csv", "r", encoding="utf-8-sig") as csvdata:
    csvdata.readline()
    for list in csvdata:
        parts = list.strip().split(",")
        records.append(parts)

for data in records:
    country.add(data[countryNumber])
    try:
        champion[data[championNumber]] += 1
    except KeyError:
        champion[data[championNumber]] = 1

print("Wimbledon Champions: ")
for name, counter in champion.items():
    print(name, counter)
print(f"\nThese {len(country)} countries have won Wimbledon: ")
print(". ".join(title for title in sorted(country)))
