file = open("input.txt")
data = list(map(int, file.readlines()))

listResult = []
result = 0

for i in range(len(data)):
    if (i + 2) < len(data):
        listResult.append(data[i] + data[i + 1] + data[i + 2])

for i in range(len(listResult)):
    if i != 0:
        if listResult[i] - listResult[i - 1] > 0:
            result += 1

print(result)
