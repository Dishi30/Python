import random
from art import logo
from words import word_list

chosen_word = random.choice(word_list)
print(f"word is: {chosen_word}")
display = []
end_of_game = False
lives = 5

for i in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print("You've already guessed")

    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from art import stages
    print(stages[lives])