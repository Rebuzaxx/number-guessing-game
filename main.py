import random
play_again = "yes"
while play_again == "yes":

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You Guessed it!")
            print("Total attempts:", attempts)
            break

        elif guess > number:
            print("Too High!")
        
        else:
            print("Too Low!")

    if guess != number:
        print("Game Over!")
        print("The Correct number was:", number)
        
    play_again = input("Play again?(yes/no):").lower()

print("Thanks for playing!") 