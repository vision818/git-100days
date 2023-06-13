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

login()






# def roll_dice():
#     import random
#     dice = random.randint(1,6)
#     print ("You rolled", dice)
# for i in range(100):
#      roll_dice()