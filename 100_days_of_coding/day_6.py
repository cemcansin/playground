import random

#randomly pick a word
list_of_words = ["computer", "morphology", "fantastic"]
word = random.choice(list_of_words)

placeholde = ""
word_length = len(word)
placeholde * len(word)
print(placeholde)

game_over = False
correct_letters = []

while not game_over:
    guess = input("guess a letter\n").lower()

    display = ""

    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if "_" not in display:
        game_over = True
        print("You win. ")


