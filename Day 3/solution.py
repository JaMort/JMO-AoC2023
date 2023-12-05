import re

#setup
input = open('input.txt', 'r')
lines = input.read().splitlines()
input.close()

# part 1 - find the sum of all engine numbers that are adjacent (even diagonally) to a symbol
part_numbers = []
for i, line in enumerate(lines):
    line_above = None
    line_below = None
    if i != 0:
        line_above = lines[i-1]
    if i != len(lines) -1:
        line_below = lines[i+1]
    numbers_in_line = [int(s) for s in re.findall(r'\d+', line)]
    for number in numbers_in_line:
        adjacent = ''
        index = line.index(str(number))
        index_end = index + len(str(number)) + 3 if index == 0 else index + len(str(number))
        if index > 0:
            index = index-1
        if index_end < len(line)-1:
            index_end = index_end+1
        if line_above != None:
            adjacent += line_above[index: index_end]
        if line_below != None:
            adjacent += line_below[index: index_end]
        adjacent += line[index: index_end]
        if any(n != '.' for n in adjacent):
            part_numbers.append(number)

print(sum(part_numbers))