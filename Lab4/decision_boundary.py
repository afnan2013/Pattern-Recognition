n = int(input("Please Enter the Feature number : "))
train_length = int(input("Please Enter the training number : "))
trainSet = []
for i in range(train_length):
    row = input().split(" ")
    row = list(map(int, row))
    trainSet.append(row)

w0 = 0
w1 = 0
w2 = 0
c = 0

while 1:
    error = False
    for i in range(train_length):
        c = c + 1
        D = w0 + w1*trainSet[i][0] + w2 * trainSet[i][1]
        if (D < 0 and trainSet[i][2] < 0) or (D >= 0 and trainSet[i][2] >= 0):
            f = "No error"
            print(i, f)
        else:
            error = True
            w0 = w0 + trainSet[i][2]
            w1 = w1 + trainSet[i][0] * trainSet[i][2]
            w2 = w2 + trainSet[i][1] * trainSet[i][2]
            print(i, w0, w1, w2)
    print(error)
    if not error:
        break

print("Number of Iteration : " + str(c))
print("D = "+str(w0)+" + "+str(w1)+"x1 + "+str(w2)+" x2")
