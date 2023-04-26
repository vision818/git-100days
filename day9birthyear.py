print("Generation Identifier!")
print(" ")
birth_year = int(input("Which year were you born? "))

if birth_year <= 1883:
    print("Extinct Generation!")
elif birth_year >= 1883 and birth_year <= 1900:
    print("Lost Generation!")
elif birth_year >= 1901 and birth_year <= 1927:
    print("Greatest Generation!")
elif birth_year >= 1928 and birth_year <= 1945:
    print("Silent Generation!")
elif birth_year >= 1946 and birth_year <= 1964:
    print("Baby Boomers!")
elif birth_year >= 1965 and birth_year <= 1980:
    print("Generation X!")
elif birth_year >= 1981 and birth_year <= 1996:
    print("Millennials!")
elif birth_year >= 1997 and birth_year <= 2012:
    print("Generation Z!")
else:
    print("Generation Alpha!")
