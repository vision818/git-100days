import random

def countdowmn(value):
    for i in range(value):
        print(i)
    
def login():

    print("REPLIT login sysytem")
    while True:

        username = input("What is your username: ")
        password = input("What is your password: ") 
        if username == "David" and password == "Replit4ever":
         print("WELCOME TO replit")
         break
        else:
         print("That is not correct one, Try Again! ")
         continue

def rollDice(sides):
  result = random.randint(1,sides)
  return result



def color_change(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")
  
def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

