import time
import random

print("Dice Simulator")
time.sleep(2)


i = True

while i == True:
    input("Press enter to roll the dice: ")
    dice_choice = random.choice(range(1, 7))
    print(f"It was: {dice_choice}")
