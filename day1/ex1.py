file = open("input.txt")
data = list(map(int, file.readlines()))
result = 0

for i in range(len(data)):
    if i != 0:
        if data[i] - data[i - 1] > 0:
            result += 1
print(result)
