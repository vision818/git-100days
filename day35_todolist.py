# my_agenda = []

# def printlist():
#     print()
#     for item in my_agenda:
#         print(item)
#     print()

# again = "yes"
# ask = "add"
# while again == "yes":
#     ask = input("add or remove? ")
#     if ask == "add":
#         item = input("Add you item to the list: ")
#         my_agenda.append(item)
#     else:
#         print(f"What do you want to remove? ")
#         printlist()
#         remove_item = input("What do you want to remove? ")
#         if remove_item in my_agenda:
#             my_agenda.remove(remove_item)
#         else:
#             print("was not in the list.")
#     again = input("Again?")

# printlist()



print("ToDo List manager")

todo_list = []

def printlist():
    print()
    for item in todo_list:
        print(item)
    print()
ask = ("view")
ask = input("Do you want to view, add or edit the list? ")
print()

while ask == "view" or "add" or "remove":
    if ask == "view":
        if todo_list == None:
            print('The list is empty, add smthg.')
        else:
            printlist()
        ask = input("Do you want to view, add or edit the list? ")
        print()

    elif ask == "add":
        again = "yes"
        while again == "yes":
            item = input("Add your item to the list: ")
            if item in todo_list:
                print("It's already there!")
            todo_list.append(item)
            again = input("add Again?")
        ask = input("Do you want to view, add or edit the list? ")
        print()

    elif ask == "edit":
        print(f"What do you want to remove? ")
        printlist()
        remove_item = input("What do you want to remove?")
        if remove_item in todo_list:
            sure = input(f"Are you sure you wanr to remove {remove_item}")
            if sure == "yes":
                todo_list.remove(remove_item)
                print(f"{remove_item} is removed!")


        else:
            print("was not in the list.")

        
        ask = input("Do you want to view, add or edit the list? ")
        print()

    

    else:
        break



#################


