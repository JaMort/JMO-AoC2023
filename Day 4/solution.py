import re

input = open('input.txt', 'r')
lines = input.read().splitlines()
input.close()


# part 1 - find the score of each card
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

def add_cards(matrix, i, n):
    for j in range(1, n + 1):
        if i + j < len(matrix) - 1:
            matrix[i + j][1] += 1
    return matrix

mpg = []
point_sum = 0
for line in lines:
    removed_cardnumber = line.split(':')[1]
    split_line = get_numbers(removed_cardnumber)
    mpg.append(find_wins(split_line))

for match in mpg:
    point_sum += get_points(match)

print(point_sum)

# part 2 - Figure out how many total scratchcards I have

scratch_matrix = []
for n in range(0, len(lines)):
    scratch_matrix.append([n, 1, 0])

matches = []
for line in lines:
    r_c = line.split(":")[1]
    s_l = get_numbers(r_c)
    matches.append(find_wins(s_l))
    for i, match in enumerate(matches):
        scratch_matrix[i][2] = match

for i, e in enumerate(scratch_matrix):
    for j in range(e[1]):
        scratch_matrix = add_cards(scratch_matrix, i, e[2])

total = 0
for card in scratch_matrix:
    total += 1 + card[2] * card[1]

print(total)