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