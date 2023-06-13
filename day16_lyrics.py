# while True:
#   print("The program is running")
#   ask = input("go again? : ")
#   if ask == "no":
#     break
# print("bye")
count = 1
print("""Fill-in the blank Lyrics!
(type in the blank lyrics and see if you are as cool as me.)""")
while True:
  word = input("Never going to_____you up : ")
  if word != "give":
    print("Nope! go again.")
    count += 1
  else:
    break
print("well done, it took you", count, "attempts!")