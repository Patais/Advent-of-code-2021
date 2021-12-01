file = open("input.txt")
data = file.readlines()
result = 0

for i in range(len(data)):
    if i != 0:
        if int(data[i]) - int(data[i - 1]) > 0:
            result += 1
print(result)
