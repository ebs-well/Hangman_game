# This was built as one of the projects from the 100 days of Python Course.
# The primary skills on display are: for loops, while statements, and if else

import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)
# Testing code
# print(f'Hey Link, the solution is {chosen_word}.')

# Creates the blank spaces so the player knows word length
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, this will print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    # This section will check the guessed letter against the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        # helps for testing purposes
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user's guess is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"{guess} is not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    from hangman_art import stages
    print(stages[lives])