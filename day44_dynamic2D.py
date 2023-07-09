# list = []

# def pretty_print():
#     print()
#     for row in list:
#         for item in row:
#             print(f"{item:^10}", end=" | ")
#         print()
#     print()

# while True :

#     exit = input("add? y/n : ")
#     if (exit.lower().strip()[0]=="y"):
#         name  = input("What is your name? : ")
#         age   = input("What is your age? : ")
#         pref  = input("What is your computer platform? : ")
#         row   = [name, age, pref]
#         list.append(row)
#     else:
#         name = input("Name of the record to delete. : ")
        
#         for row in list:
#             if name == row:
#                 list.remove(row)
#         pretty_print()




import random, os, time

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()

def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  
  numbers.sort()
  
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")
 