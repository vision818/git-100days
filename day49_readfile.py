
import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]


f = open("high.score", "r")
while True:
  contents = f.readline().strip()
  contents.split()

  if contents == "":
    break
  print(contents)

f.close()

time.sleep(3) # pause for three seconds before printing the result

print("The winner is", name, "with", highscore)