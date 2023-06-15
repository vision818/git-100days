import random, time, os

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_12():
  roll_6_sided_dice = rollDice(6)
  roll_12_sided_dice = rollDice(12)
  health = (roll_6_sided_dice * roll_12_sided_dice)/2 + 10
  return health

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  strength = (roll_6_sided_dice * roll_8_sided_dice)/2 + 12
  return strength

print("⚔️Character Builder⚔️")
time.sleep(1)
os.system("clear")
  


    #######################################################char1

character1 = input("Name your Legend: ")
type1 = input("character type(Human, Elf, Wizard, Orc): ")
print(character1)
time.sleep(1)

health1 = (roll_6_and_12())
print("HEALTH :", health1)
time.sleep(1)

strength1 = (roll_6_and_8())
print("STRENGTH :", strength1)
time.sleep(1)
#######################################################char2
print("Who are they battling? ")
character2 = input("Name your Legend: ")
type2 = input("character type(Human, Elf, Wizard, Orc): ")
print(character2)
time.sleep(1)

health2 = (roll_6_and_12())
print("HEALTH :", health2)
time.sleep(1)

strength2 = (roll_6_and_8())
print("STRENGTH :", strength2)
time.sleep(1)


char1_dice = rollDice(6)
char2_dice = rollDice(6)

round = 1
winner = None
# while health1 or health2 > 0:
while True:
  
  time.sleep(3)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  char1_dice = rollDice(6)
  char2_dice = rollDice(6)

  difference = abs(strength1 - strength2) + 1

  if char1_dice < char2_dice:
    health1 -= difference
    if round == 1:
      print(character2, "wins the first blow")
    else:
      print(character2, "wins round", round)

  elif char1_dice > char2_dice:
    health2 -= difference
    if round == 1:
      print(character1, "wins the first blow")
    else:
      print(character1, "wins round", round)

  else:
    print("It's a draw on round", round)
    
  print()
  print(character1)
  print("HEALTH:", health1)
  print()
  print(character2)
  print("HEALTH:", health2)
  print()

  if health1<=0:
    print(character1, "has died!")
    winner = character2
    break
  elif health2<=0:
    print(character2, "has died!")
    winner = character1
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")



