import random, os, time

list_of_words = ["grudge", "frozen", "resignation", "proportion", "polish", "tribe", "grateful", "inappropriate", "quite", "disgrace"]
letter_picked = []
lives = 6

random_word = random.choice(list_of_words)

while True:
    time.sleep(1)
    os.system("clear")
    random_letter = input('choose a letter which you think is in the word : ')

    print(random_word)

    if random_letter in letter_picked:
        print("You've tried that before")
        continue
    
    letter_picked.append(random_letter)

    if random_letter in random_word:
        print("You found a letter")
    else:
        print("Nope, not in there")
        lives -= 1
  
    all_letters = True

    for i in random_word:
        if i in random_letter:
            print(i, end = '')
        else:    
            print("_", end ='')
            all_letters = False
    print()

    if all_letters:
        print(f"You won with {lives} left!")
        break

    if lives<=0:
        print(f"You ran out of lives! The answer was {random_word}")
        break
    else:
        print(f"Only {lives} left")




