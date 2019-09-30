n = int(input("Please input the train data row : "))
k = int(input("Please input the value of K : "))

trainSet = [[4, 4], [8, 4], [15, 8], [20, 6], [21, 10],[24, 4], [24, 12]]


centroid = []
centroid.append(trainSet[0])
centroid.append(trainSet[2])
centroid.append(trainSet[4])

t = 2
#while t:
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

    for j in range(k):
        sumx = 0
        sumy = 0
        num = 0
        for p in range(len(temp)):
            if temp[p][1] == j:
                sumx += trainSet[p][0]
                sumy += trainSet[p][1]
                num += 1
        if num > 0:
            x = sumx / num
            y = sumy / num
            centroid[j] = [x, y]

    print(str(i)+"  ("+str(trainSet[i][0])+", "+ str(trainSet[i][1])+")  ("+str(centroid[index][0])+", "+str(centroid[index][1])+")")
    print(centroid)
    #t = t-1