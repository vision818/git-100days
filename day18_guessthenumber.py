print ("One million to one! ")
count = 1

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
  elif guess < 60000:
    print ("Low!")
    count = count + 1
  elif guess > 60000:
    print ("High!")
    count = count + 1
    continue
  elif guess == 60000:
    print ("Success!!")
    print ("It took you ", count , " counts to get here.")
    break
  else:
    print(" NO way!")
    count = count + 1
