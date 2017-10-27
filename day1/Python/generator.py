import random

def roll_die():
    dice = []
    dice_number = [1, 2, 3, 4, 5, 6]
    while True:
        i = random.choice(dice_number)
        dice.append(i)
        dice_number.remove(i)
        if len(dice) == 6:
            yield dice
            dice = []
            dice_number = [1, 2, 3, 4, 5, 6]


print(next(roll_die()))
