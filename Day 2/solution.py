import re

#setup
input = open('input.txt', 'r')
lines = input.read().splitlines()
input.close()

# part 1 - find how many games (lines) are viable with a maximum of: 12 red, 13 green and 14 blue.

games = []

for line in lines:
    line_substrings = line.split(':')
    game = line_substrings[0]
    results = line_substrings[1].split(';')
    game = [int(s) for s in re.findall(r'\d+', game)]
    is_possible = True
    for result in results:
        values = result.split(',')
        for value in values:
            if value.__contains__('red'):
                number = [int(s) for s in re.findall(r'\d+', value)]
                if number[0] > 12:
                    is_possible = False
                    break
            elif value.__contains__('green'):
                number = [int(s) for s in re.findall(r'\d+', value)]
                if number[0] > 13:
                    is_possible = False
                    break
            elif value.__contains__('blue'):
                number = [int(s) for s in re.findall(r'\d+', value)]
                if number[0] > 14:
                    is_possible = False
                    break
        if not is_possible:
            break
    games.append([game[0], is_possible])

possible_games = [key for key, value in games if value]
print(sum(possible_games))

# part 2 - find the power (numbers multiplied together) of each minimum set of cubes that must be present in the games

games2 = []

for line in lines:
    line_substrings = line.split(':')
    results = line_substrings[1].split(';')
    min_red = 0
    min_green = 0
    min_blue = 0
    for result in results:
        values = result.split(',')
        for value in values:
            if value.__contains__('red'):
                number = [int(s) for s in re.findall(r'\d+', value)][0]
                if number > min_red:
                    min_red = number
            elif value.__contains__('green'):
                number = [int(s) for s in re.findall(r'\d+', value)][0]
                if number > min_green:
                    min_green = number
            elif value.__contains__('blue'):
                number = [int(s) for s in re.findall(r'\d+', value)][0]
                if number > min_blue:
                    min_blue = number
    games2.append(min_red * min_green * min_blue)

print(sum(games2))
