
print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
print(first)
last = all[1].strip()
print(last)
maiden = all[2].strip()
print(maiden)
city = all[3].strip()
print(city)


name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")