file = open("input.txt")
data = file.readlines()

position = 0
depth = 0
aim = 0

for i in range(len(data)):
    if len(data[i]) == 7:   # DOWN
        depth += int(data[i][5:6])
    elif len(data[i]) == 10:    # FORWARD
        position += int(data[i][8:9])
        aim += int(data[i][8:9]) * depth
    else:   # UP
        depth -= int(data[i][3:4])

print(position * aim)
