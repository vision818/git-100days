print("Loan calculator")
initial_amount = 1000
lent_money = 1000
tenure = 10
percentage = 5


for i in range(tenure):
  i=i+1
  lent_money = (lent_money + ( lent_money * percentage)/100)
  print("Year", i , "is", lent_money)

print("You paid ", round(lent_money - initial_amount, 2), "in interest!")