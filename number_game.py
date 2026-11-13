
import random

print("==============================")
print("     NUMBER GUESSING GAME")
print("==============================")

while True:
    computer = random.randint(1, 100)
    attempts = 0

    print("\nGuess a number between 1 and 100")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100!")
            continue

        attempts += 1

        if guess == computer:
            print("\nCONGRATULATIONS!")
            print("You guessed the correct number!")
            print("Total attempts:", attempts)
            break
        elif guess < computer:
            print("Too low! Try a bigger number.")
        else:
            print("Too high! Try a smaller number.")

    print("\nYour score:", max(0, 100 - attempts * 5))

    again = input("\nPlay again? (yes/no): ")

    if again.lower() != "yes":
        print("\nTHANK YOU FOR PLAYING!")
        print("GAME OVER")
        break
