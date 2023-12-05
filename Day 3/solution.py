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
        index_end = index + len(str(number))
        print("line: " + str(i) + " number: " + str(number) + " index_start: " + str(index) + " index_end: " + str(index_end))
        if index > 0:
            index = index-1
        if index_end < len(line):
            index_end = index_end+1
        part_numbers.append(number)