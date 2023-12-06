import re

#setup
input = open('input.txt', 'r')
lines = input.read().splitlines()
input.close()

def get_surrounding(matrix, row, col):
    surroundings = []
    if 1 < row:
        surroundings += matrix[row-1][max(0, col[0] - 1):min(col[1]+1, len(matrix[0]))]
    if row < len(matrix) - 1:
        surroundings += matrix[row + 1][max(0, col[0] - 1):min((col[1] + 1, len(matrix[0])))]
    surroundings += matrix[row][max(0, col[0]-1):col[0]]
    surroundings += matrix[row][col[1]:min(col[1] + 1, len(matrix[0]))]

    return surroundings

def get_gear_position(matrix, row, col):
    if 1 < row:
        for i in range(max(0, col[0]-1), min(col[1] + 1, len(matrix[0]))):
            if matrix[row - 1][i] == '*':
                return row - 1, i
    if row < len(matrix) - 1:
        for i in range(max(0, col[0] - 1), min(col[1] + 1, len(matrix[0]))):
            if matrix[row + 1][i] == '*':
                return row + 1, i
    if col[0] > 0:
        if matrix[row][col[0] - 1] == '*':
            return row, col[0] - 1
    if col[1] < len(matrix[0]):
        if matrix[row][col[1]] == '*':
            return row, col[1]
    
    return -1, -1

# part 1 - find the sum of all engine numbers that are adjacent (even diagonally) to a symbol
sum = 0
for r, line in enumerate(lines):
    for number in re.finditer(r'\d+', line):
        n = int(number.group())
        s = get_surrounding(lines, r, number.span())
        s = ''.join(s)
        if re.search(r'[^0-9.]', s):
            sum += n

print(sum)

# part 2 - find the sum of all gear ratios (gears are * surrounded by numbers, gear ratio is the multiplication of these)

gr_sum = 0
gears = []
for r, line in enumerate(lines):
    for number in re.finditer(r'\d+', line):
        n = int(number.group())
        s = get_surrounding(lines, r, number.span())
        s = ''.join(s)
        if '*' in s:
            gp = get_gear_position(lines, r, number.span())
            gears.append([n, gp, 0])

for i, gear in enumerate(gears):
    loc = gear[1]
    for j in range(i + 1, len(gears)):
        if gears[j][1] == loc:
            gr_sum += gear[0] * gears[j][0]
            gears[i][2] = 1
            gears[j][2] = 1

print(gr_sum)