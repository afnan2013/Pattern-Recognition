import arff
import pandas as pd
import math
import numpy as np
from scipy import stats


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


k = int(input("Please input your K : "))

# ************Wine Code***********************

filename = "wine"+str(k)+".txt"
file_wine = open(filename, "w+")
trainData = arff.load('wine_train.arff')
testData = arff.load('wine_test.arff')
trainDataPd = pd.DataFrame(trainData)
testDataPd = pd.DataFrame(testData)

r = 1
sum_d = 0
for each in testDataPd.itertuples():
    distances = eucleadian_distance(each, trainDataPd, 12)
    responses = []
    for p in range(k):
        responses.append(distances[p][1])
    mean = np.mean(responses)
    sum_d += abs(mean-each[12])
    print(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12]))
    file_wine.write(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12])+"\n")
    r += 1

print_regression_result(sum_d/(r-1), r-1)
file_wine.close()


# *****************Yeast Code Starts*****************
filename = "yeast"+str(k)+".txt"
file_yeast = open(filename, "w+")
trainData1 = arff.load('yeast_train.arff')
testdata1 = arff.load('yeast_test.arff')
trainDataPd1 = pd.DataFrame(trainData1)
testDataPd1 = pd.DataFrame(testdata1)

n = 1
c = 0
for each in testDataPd1.itertuples():
    distances = eucleadian_distance(each, trainDataPd1, 9)
    responses = []
    for p in range(k):
        responses.append(distances[p][1])
    mode = stats.mode(responses)
    if mode[0][0] == each[9]:
        c += 1
    print(str(n)+" Predicted Class: "+str(mode[0][0])+"    Actual Class : "+str(each[9]))
    file_yeast.write(str(n)+" Predicted Class: "+str(mode[0][0])+"    Actual Class : "+str(each[9])+"\n")
    n += 1
print_class_result(c, n-1)
file_yeast.close()