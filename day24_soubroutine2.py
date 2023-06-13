import random
print ("Infinity Dice!")
sides = int(input("How many sides? "))
def roll_dice(sides):
    while True:
        

        number = random.randint(0, sides)
        print("You rolled", number)

        ask = input("Roll again? ")
        if ask == "yes":
            continue
        else:
            break

roll_dice(sides)
