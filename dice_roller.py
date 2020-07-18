import random
dice_sum = 0
dice_roll = 2
#"for every index in a range starting after 0 until the value
#is equal to dice_rolls, do this:"
for i in range (0,dice_roll):
    roll = random.randint(1,6)
    dice_sum += roll # a shorter way of writing this: dice_sum = dice_sum + roll
    if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')
    elif roll == 6:
        print(f'You rolled a {roll}! Critical Success!')
    else:
        print(f'You rolled a {roll}')
print(f'You have rolled a total of {dice_sum}')
