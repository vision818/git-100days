print("""Wholesome Positivity Machine


""")

name = input ("who are you? ")
goal = input ("What do you want to achieve? ")
feel = input ("On a scale of 1-10, how do you feel today? ")

if feel < "5":
  print("""Hey""", name, """, keep your chin up! Today you are going to""", goal, """! in the most amazing way, simply by being you!! --you ROCK!""")

elif feel == "5" or feel == "6":
  print("""Hey""", name, """, you need a little push! Today you are going to""", goal, """! in the most amazing way, simply by being you!! --you ROCK!""")

else:
  reason = input("what is the reason honey?")
  if reason == "nothing":
    print (" it is okay if you do not want to share!")
  else:
    print("wow!")
  