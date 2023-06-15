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
  

Again = "yes"

while Again == "yes":
  character = input("Name your Legend: ")
  type = input("character type(Human, Elf, Wizard, Orc): ")

  print(character)
  time.sleep(1)

  health = str(roll_6_and_12())
  print("HEALTH :", health)
  time.sleep(1)
  
  strength = str(roll_6_and_8())
  print("STRENGTH :", strength)
  time.sleep(1)
  os.system("clear")

  print("May your name go down in legend.")


  print("Their health is ", health,"hp" ) 
  Again = input("Again?")