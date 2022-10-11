import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)
word_length = len(chosen_word)
lives = 6

display = []
for letter in range(word_length):
    display.append("_")

end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    if user_guess in display:
        print("You've already guessed this letter")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter in user_guess:
           display[position] = letter

    if user_guess not in chosen_word:
        print("This letter is not in the word, You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print({f"Game Over! The word is {chosen_word}"})
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win.")
    print(stages[lives])
