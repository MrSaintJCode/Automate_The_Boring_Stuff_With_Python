import random
import time
import sys

lives = 10
randomNumber = random.randint(1,20)

while lives >= 1:
    print("")
    try:
        print(f"Current Lives - {lives}")
        lives = lives - 1
        guess = int(input("I am thinking of a number between 1 and 20.\nGuess(1-20): "))
    
        if guess == randomNumber:
            print("")
            print("------> Winner Winner Chicken Dinner! <------")
            print(f"The Number was - {guess}")
            sys.exit()
        elif guess > randomNumber:
            print("")
            print("[X] The Number is lower")
        elif guess < randomNumber:
            print("")
            print("[X] The Number is higher")
        else:
            print("")
            print("[X] Wrong Number - Please Try Again")
    except ValueError:
        print("")
        print("[X] Please Enter a Number (1-20)")
        

print("")
print("[X] You Have Died!")