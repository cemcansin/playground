import random
stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]
# Words
list_of_words = ["computer", "morphology", "fantastic"]
word = random.choice(list_of_words)

correct_letters = []
lives = 6
game_over = False

print("_" * len(word))

while not game_over:
    guess = input("Guess a letter:\n").lower()

    if guess in word and guess not in correct_letters:
        correct_letters.append(guess)
    elif guess not in word:
        lives -= 1
        print("Wrong guess!")
        print(f"Lives remaining: {lives}")
        print(stages[6 - lives])

    # Build display
    display = ""
    for letter in word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("You win! 🎉")
        game_over = True

    if lives <= 0:
        print("You lost! 😢 The word was:", word)
        game_over = True
