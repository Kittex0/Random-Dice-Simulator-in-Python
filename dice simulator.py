# These are the modules needed, the time module is customary while the random module in mandotory
import time
import random

# Intro
print("Dice Simulator")
time.sleep(2)


i = True


while i == True:
    # Chooses the random number from 1-6 and then displays it.
    input("Press enter to roll the dice: ")
    dice_choice = random.choice(range(1, 7))
    print(f"It was: {dice_choice}")
