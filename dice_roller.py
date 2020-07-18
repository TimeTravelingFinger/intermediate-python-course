import random
dice_sum = 0
dice_roll = 2
#"for every index in a range starting after 0 until the value
#is equal to dice_rolls, do this:"
for i in range (0,dice_roll):
# def main():
    roll = random.randint(1,6)
    dice_sum += roll # a shorter way of writing this: dice_sum = dice_sum + roll
    print(f'You rolled a {roll}')
print(f'You have rolled a total of {dice_sum}')

# if __name__== "__main__":
#   main()
