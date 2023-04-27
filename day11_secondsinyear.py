print ("seconds in a year!")

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

seconds_in_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

seconds_in_leap_year = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute

leap_year = input("is it a leap year? ")

if leap_year == "yes":
  print("There are ",seconds_in_leap_year," in a leap year. ")
else:
  print("There are ",seconds_in_year," in a year. ")