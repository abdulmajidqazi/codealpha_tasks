import random

words = ["python", "computer", "program", "hangman", "keyboard"]
word = random.choice(words)

guessed_letters = []
max_wrong_guesses = 6
wrong_guesses = 0
display = ["_"] * len(word)

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Incorrect!")

if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)