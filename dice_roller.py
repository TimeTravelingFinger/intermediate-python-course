import random
print('What is up bro! What is your team name?')
team_name = input()
print('What is the second team name?')
team_name_two = input()
print('How is it going, ' + team_name + ' and ' + team_name_two + " let's get rolling!")
team_name_total = 0
team_name_two_total =0
dice_sum_team = 0
dice_sum_team_two = 0
dice_roll = 2
#"for every index in a range starting after 0 until the value
#is equal to dice_rolls, do this:"
for team_name_roll in range (0,dice_roll):
    roll = random.randint(1,6)
    dice_sum_team += roll # a shorter way of writing this: dice_sum = dice_sum + roll
    if roll == 1:
        print(team_name + f', You rolled a {roll}! Critical Fail')
    elif roll == 6:
        print(team_name + f', You rolled a {roll}! Critical Success!')
    else:
        print(team_name + f', You rolled a {roll}')
print(team_name + f', rolled a total of {dice_sum_team}')

for team_name_two_roll in range (0,dice_roll):
    roll = random.randint(1,6)
    dice_sum_team_two += roll # a shorter way of writing this: dice_sum = dice_sum + roll
    if roll == 1:
        print(team_name_two + f', You rolled a {roll}! Critical Fail')
    elif roll == 6:
        print(team_name_two + f', You rolled a {roll}! Critical Success!')
    else:
        print(team_name_two + f', You rolled a {roll}')
print(team_name_two + f', rolled a total of {dice_sum_team_two}')
