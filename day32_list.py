# #lists


# timetable = ["computer science", "math", "english", "art", "sport"]
# for i in range(len(timetable)):
#     timetable[2] = "no"
#     print(timetable[i:])

# while True:
#       print(timetable[i:])
#       break

import random

greetings = ["Hello there!", "Konichiwa!", "Guten Tag!", "Bonjour", "Namaste!"]
randomgreet = greetings[random.randint(0, len(greetings)-1)]
print(randomgreet)