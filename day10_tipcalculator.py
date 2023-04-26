print("Tip Calculator")

spent = float(input("How much did you spend?"))
tip = int(input("What percentage do you want to tip?"))
people = int(input("How many people in your grp?"))

answer = (spent + ((spent * tip) / 100)) / people
answer = round( answer, 2)
print("You each owe $", answer)
