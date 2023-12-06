import re

input = open('input.txt', 'r')
lines = input.read().splitlines()
input.close()


def get_numbers(line):
    split_line = line.split('|')
    winning_numbers = re.findall(r'\d+', split_line[0])
    game_numbers = re.findall(r'\d+', split_line[1])
    return [winning_numbers, game_numbers]

def find_wins(v):
    matches = 0
    for number in v[1]:
        if number in v[0]:
            matches += 1
            continue
    return matches

def get_points(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return 2 * get_points(n-1)

# part 1 - find the score of each card
mpg = []
point_sum = 0
for line in lines:
    removed_cardnumber = line.split(':')[1]
    split_line = get_numbers(removed_cardnumber)
    mpg.append(find_wins(split_line))

for match in mpg:
    point_sum += get_points(match)

print(point_sum)

