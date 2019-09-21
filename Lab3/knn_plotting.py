import arff
import pandas as pd
import math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def print_class_result(correct, total):
    print("Number of correctly classified instances : ", correct)
    print("Total number of instances : ", total)
    print("Accuracy : ", correct / total)
    file_yeast.write("Number of correctly classified instances : "+
                     str(correct)+"\nTotal number of instances : "+
                     str(total)+"\nAccuracy : "+str(correct / total))


def print_regression_result(mae, total):
    print("Mean absolute error : ", mae)
    print("Total number of instances : ", total)
    file_wine.write("Mean absolute error : "+str(mae)+"\nTotal number of instances : "+str(total))


def eucleadian_distance(test, trainset, classifier_index):
    distances = []
    for row in trainset.itertuples():
        add = 0
        for i in range(1, len(trainset.columns)-1):
            add += math.pow(test[i]-row[i], 2)
        add = math.sqrt(add)
        distances.append([add, row[classifier_index]])
    distances.sort(key=lambda x: x[0])
    return distances


k = [1, 2, 3, 5, 10]

filename = "wine"+str(k)+".txt"
file_wine = open(filename, "w+")
trainData = arff.load('wine_train.arff')
testData = arff.load('wine_test.arff')
trainDataPd = pd.DataFrame(trainData)
testDataPd = pd.DataFrame(testData)

error = []
for k_each in k:
    r = 1
    sum_d = 0
    for each in testDataPd.itertuples():
        #print(each)
        distances = eucleadian_distance(each, trainDataPd, 12)
        responses = []
        for p in range(k_each):
            responses.append(distances[p][1])
        mean = np.mean(responses)
        sum_d += abs(mean-each[12])
        print(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12]))
        r += 1
    print_regression_result(sum_d/(r-1), r-1)
    error.append(sum_d/(r-1))

file_wine.close()

f = plt.figure(1)
plt.plot(k, error, label="k vs error Line")
plt.xlabel('K')
plt.ylabel('Absolute error')
plt.title('Two lines on same graph!')


k2 = [1, 5, 10, 20, 30]

filename = "yeast"+str(k)+".txt"
file_yeast = open(filename, "w+")
trainData1 = arff.load('yeast_train.arff')
testData1 = arff.load('yeast_test.arff')
trainDataPd1 = pd.DataFrame(trainData1)
testDataPd1 = pd.DataFrame(testData1)

accuracy = []
for k_each in k2:
    n = 1
    c = 0
    for each in testDataPd1.itertuples():
        #print(each)
        distances = eucleadian_distance(each, trainDataPd1, 9)
        responses = []
        for p in range(k_each):
            responses.append(distances[p][1])
        mode = stats.mode(responses)
        if mode[0][0] == each[9]:
            c += 1
        print(str(n)+" Predicted Value: "+str(mode[0][0])+"    Actual Value : "+str(each[9]))
        file_yeast.write(str(n)+" Predicted Value: "+str(mode[0][0])+"    Actual Value : "+str(each[9])+"\n")
        n += 1
    print_class_result(c, n-1)
    accuracy.append(c/(n-1))
file_yeast.close()

p = plt.figure(2)
plt.plot(k2, accuracy, label="k vs Accuracy Line")
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.title('Accuracy of Classification with K Graph')

plt.show()

input()