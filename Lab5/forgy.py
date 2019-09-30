n = int(input("Please input the train data row : "))
k = int(input("Please input the value of K : "))

trainSet = [[4, 4], [8, 4], [15, 8], [20, 6], [21, 10],[24, 4], [24, 12]]

centroid = []
centroid.append(trainSet[0])
centroid.append(trainSet[2])
centroid.append(trainSet[4])
print(centroid)
results = [0 for i in range(k)]
while 1:
    temp = []
    results_temp = [0 for i in range(k)]
    for i in range(n):
        sample = trainSet[i]
        mini = 10000
        index = 0
        for j in range(k):
            cd = abs(sample[0] - centroid[j][0]) + abs(sample[1] - centroid[j][1])
            if cd < mini:
                mini = cd
                index = j
                results_temp[j] += 1
        temp.append([i, index])
        print(str(i)+"  ("+str(trainSet[i][0])+", "+ str(trainSet[i][1])+")  ("+str(centroid[index][0])+", "+str(centroid[index][1])+")")
    flag = True
    for i in range(k):
        if results[i] != results_temp[i]:
            flag = False
    if flag:
        break
    for i in range(k):
        sumx = 0
        sumy = 0
        num = 0
        for j in range(n):
            if temp[j][1] == i:
                sumx += trainSet[j][0]
                sumy += trainSet[j][1]
                num += 1
        x = sumx / num
        y = sumy / num
        centroid[i] = [x, y]
    print(centroid)
    results = results_temp