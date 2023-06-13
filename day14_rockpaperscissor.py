from getpass import getpass as input

print ("E P I C  B A T T L E")
print (" Select your move. R, P or S")

player_1  = input("Player 1 > ")
player_2  = input("Player 2 > ")

if player_1 == "R" and player_2 == "P":
  print ("Player 2 wins!")
elif player_1 == "P" and player_2 == "S":
  print ("Player 2 wins!")
elif player_1 == "S" and player_2 == "R":
  print ("Player 2 wins!")
else:
  print ("Player 1 wins!")