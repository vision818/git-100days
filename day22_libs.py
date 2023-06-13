import random


print ("One million to one! ")
count = 1
random_number = random.randint(59999, 60100)
while True:
  guess = int(input("What is your guess? : "))
  if guess < 0:
    print(" You do not deserve this game!")
  if guess < 50000:
    print ("Too low!")
    count = count + 1
  elif guess > 75000:
    print ("Too high!")
    count = count + 1
  elif guess < random_number:
    print ("Low!")
    count = count + 1
  elif guess > random_number:
    print ("High!")
    count = count + 1
    continue
  elif guess == random_number:
    print ("Success!!")
    print ("It took you ", count , " counts to get here.")
    break
  else:
    print(" NO way!")
    count = count + 1
