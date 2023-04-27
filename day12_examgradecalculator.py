print("Exam Grade Calculator")
print(" ")
subject = input("Which subject did you give?")
print("Name of exam: ", subject)
max_score = int(input("Max possible score: "))
my_score = int(input("Your SCORE: "))

percentage = (my_score/max_score)*100
percentage = round(percentage, 2)
if percentage <= 40:
    print("You got", percentage,"% which is a\033[31m U")
elif percentage > 40 and percentage <= 50:
    print("You got", percentage,"% which is a\033[32m D")
elif percentage > 50 and percentage <= 60:
    print("You got", percentage,"% which is a\033[33m C")
elif percentage > 60 and percentage <= 70:
    print("You got", percentage,"% which is a\033[34m B")
elif percentage > 70 and percentage <= 80 :
    print("You got", percentage,"% which is a\033[35m A-")
elif percentage > 80 and percentage <= 90:
    print("You got", percentage,"% which is a\033[36m A+")
elif percentage > 90 and percentage <= 100:
    print("You got", percentage,"% which is a\033[32m A++")
else:
    print("Are you ALIEN?")
