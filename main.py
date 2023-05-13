import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

def play_hangman():
    print(logo)

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = ['_' for _ in range(word_length)]
    lives = 6
    guessed_letters = []

    while True:
        guess = input("Guess a letter: ").lower()
        clear()
        
        if guess in guessed_letters:
            print(f"You've already guessed {guess}.")
        else:
            guessed_letters.append(guess)
            if guess in chosen_word:
                for position in range(word_length):
                    if chosen_word[position] == guess:
                        display[position] = guess
            else:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    print(stages[lives])
                    print(f"The word was '{chosen_word}'.\nYou lose.\nGame Over")
                    break
            print(stages[lives])
            print(f"{' '.join(display)}")
            if "_" not in display:
                print("You win!")
                break

if __name__ == '__main__':
    play_hangman()
