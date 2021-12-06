file = open("input.txt")
data = file.readlines()

resultList = []
gamma = ""
epsilon = ""

for i in range(len(data[0]) - 1):
    resultList.append(0)

for i in range(len(data)):
    for j in range(len(data[i]) - 1):
        if data[i][j] == '1':
            resultList[j] += 1
        else:
            resultList[j] -= 1

for i in range(len(data[0]) - 1):
    if resultList[i] > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma)  # 2601
print(epsilon)  # 1494
