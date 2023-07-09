example = { "name" : None, "url" : None, "desc" : None, "rating" : None }


for name in example.keys():
   example[name] = input(f"{name}: ")

print()

for name, value in example.items():
    print(f"{name} : {value}")

    print()

print(example)