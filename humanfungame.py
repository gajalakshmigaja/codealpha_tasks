import random

# List of words
words = ["apple", "python", "computer", "school", "orange", "Winter", "Summer", "Laptop", "Spring", "Friend", "Silver"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed = []

# Number of wrong guesses
attempts = 6

print("====== HANGMAN GAME ======")
print("Guess the word one letter at a time!")

while attempts > 0:

    display = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct!")

    # Wrong guess
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

# If attempts become 0
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)