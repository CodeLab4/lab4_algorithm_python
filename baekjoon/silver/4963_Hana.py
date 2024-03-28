land_count = 0
maps = list()
input_line = ''

while input_line != '0 0':
    input_line = input()

    if len(input_line) == 3:
        w, h = input_line.split(' ')
    else:
        maps.append(input_line.split(' '))

print(maps)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

for row, col in directions:
# ...


print(land_count)
