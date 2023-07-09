print("High Score Table")


again = "yes"
while again == "yes":
        f = open("high.score", "a+")
        initials = input("Initials > ")
        score = input("score > ")

        f.write(f"{initials} {score} \n")

        print("ADDED")
        f.close()

        again = input ("again?")