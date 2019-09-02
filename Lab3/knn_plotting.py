from scipy.io import arff
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


k = [1, 2, 3, 5, 10]

filename = "wine"+str(k)+".txt"
file_wine = open(filename, "w+")

data = arff.loadarff('wine_train.arff')
test = arff.loadarff('wine_test.arff')
df = pd.DataFrame(data[0])
#print(df)
dfTest = pd.DataFrame(test[0])
#print(dfTest)

'''
error = []
for k_each in k:
    r = 1
    sum_d = 0
    for each in dfTest.itertuples():
        #print(each)
        distances = []
        for row in df.itertuples():
            add = 0
            for i in range(1, len(df.columns)-1):
                add += math.pow(each[i]-row[i], 2)
            add = math.sqrt(add)
            distances.append([add, row[12]])
        distances.sort(key=lambda x: x[0])
        responses = []
        for p in range(k_each):
            responses.append(distances[p][1])
        mean = np.mean(responses)
        sum_d += abs(mean-each[12])
        print(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12]))
        #file_wine.write(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12])+"\n")
        r += 1
    print_regression_result(sum_d/(r-1), r-1)
    error.append(sum_d/(r-1))

file_wine.close()

plt.plot(k, error, label="k vs error Line")
plt.xlabel('K')
plt.ylabel('Absolute error')
plt.title('Two lines on same graph!')
plt.show()
'''
filename = "yeast"+str(k)+".txt"
file_yeast = open(filename, "w+")

k = [1, 5, 10, 20, 30]

data1 = arff.loadarff('yeast_train.arff')
test1 = arff.loadarff('yeast_test.arff')
df1 = pd.DataFrame(data1[0])
#print(df1)
dfTest1 = pd.DataFrame(test1[0])
#print(dfTest1)

accuracy = []
for k_each in k:
    n = 1
    c = 0
    for each in dfTest1.itertuples():
        #print(each)
        distances = []
        for row in df1.itertuples():
            add = 0
            for i in range(1, len(df1.columns)-1):
                add += math.pow(each[i]-row[i], 2)
            add = math.sqrt(add)
            distances.append([add, row[9]])
        distances.sort(key=lambda x: x[0])
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

plt.plot(k, accuracy, label="k vs Accuracy Line")
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.title('Accuracy of Classification with K Graph')
plt.show()