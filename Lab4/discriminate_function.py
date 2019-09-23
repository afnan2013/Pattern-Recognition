cl = int(input("The Number of classes, Class : "))
f = int(input("The number of feature, f : "))
s = int(input("The Number of samples, s : "))
c = int(input("The Number of samples, c : "))
ka = int(input("The Number of samples, k : "))

trainSet = []
for i in range(s):
    row = input().split(" ")
    row = list(map(int, row))
    trainSet.append(row)

#functionMatrix = [[0 for i in range(f+1)] for j in range(cl)]
functionMatrix = [
    [3, 4, 5, 6],
    [7, 2, -3, 4],
    [-2, -4, 6, 8],
    [5, 6, -7, 8]
]
print(functionMatrix)

while 1:
    error = False
    for i in range(s):
        values_of_D = []
        class_actual = trainSet[i][f]
        for j in range(cl):
            D = 0
            for k in range(f+1):
                if k == 0:
                    D += functionMatrix[j][k]
                else:
                    D += functionMatrix[j][k]*trainSet[i][k-1]
            values_of_D.append([D, j])
        values_of_D.sort(key=lambda x: x[0], reverse=True)  # f is the index of class
        # i is the index of the train samples
        class_prdicted = values_of_D[0][1]
        if class_actual == class_prdicted:
            print(i, "no error")
        else:
            error = True
            for k in range(f+1):
                if k == 0:
                    functionMatrix[class_actual][k] += (c * 1 * ka)
                else:
                    functionMatrix[class_actual][k] += (c * 1 * trainSet[i][k-1])
            for k in range(f+1):
                if k == 0:
                    functionMatrix[class_prdicted][k] -= (c * 1 * ka)
                else:
                    functionMatrix[class_prdicted][k] -= (c * 1 * trainSet[i][k-1])

    print(error)
    if not error:
        break

for i in range(cl):
    print("D"+str(i), end="  ")
    for j in range(f+1):
        print(functionMatrix[i][j], end=" ")
    print("")
# print(functionMatrix)