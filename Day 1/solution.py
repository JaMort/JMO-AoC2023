input = open("./input.txt", "r")
lines = input.read().splitlines()
input.close()
num_lines = []

for line in lines:
    indexes = [i for i, x in enumerate(line) if x.isdigit()]
    first = line[indexes[0]]
    last = line[indexes[-1]]

    num_lines.append(int(first + last))

print(sum(num_lines))

# part 2

translation_dict = { 'zero': 'z0o', 'one':'o1e', 'two':'t2o', 'three': 't3e', 'four': 'f4r', 'five':'f5e', 'six':'s6x', 'seven':'s7n', 'eight':'e8t', 'nine':'n9e'}
part_2lines = []
for line in lines:
    for key, value in translation_dict.items():
        line = line.replace(key, value)
    indexes = [i for i, x in enumerate(line) if x.isdigit()]
    first = line[indexes[0]]
    last = line[indexes[-1]]

    part_2lines.append(int(first + last))

print(sum(part_2lines))