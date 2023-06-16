# name = "jeegar"
# age = 25
# pronouns = "He/him"

# print(f"this is {name}, using {pronouns} pronouns and is {age} years old. hello {name}, how are you? have you been a great {age} years so far?")

# for i in range(1,31):
#   print(f"Day{i: >2} of 100.")

print("30 days down - What did you think? ")
for i in range (1,31):
    print(f"Day {i} :")
    print()
    thought = input("")
    text = f"You thought Day {i} was"

    print(f"{text: ^35}")   
    print(f"{thought: ^35}")   