names = []

def printList():
  print()
  for name in names:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in names:
    names.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()