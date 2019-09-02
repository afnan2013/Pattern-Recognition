from scipy.io import arff
import pandas as pd
import math
import numpy as np
from scipy import stats

file_wine = open("wine357.txt", "w+")
file_yeast = open("yeast357.txt", "w+")

s_values = ""


def print_regression_result(mae, total):
    print("Mean absolute error : ", mae)
    print("Total number of instances : ", total)
    s_values += "Mean absolute error for k = : " + str(mae) + "\nTotal number of instances : " + str(total)
    #file_wine.write("Mean absolute error for k = : " + str(mae) + "\nTotal number of instances : " + str(total))


def print_class_result(correct, total):
    print("Number of correctly classified instances : ", correct)
    print("Total number of instances : ", total)
    print("Accuracy : ", correct / total)
    file_yeast.write("Number of correctly classified instances : " +
                     str(correct) + "\nTotal number of instances : " +
                     str(total) + "\nAccuracy : " + str(correct / total))


data = arff.loadarff('wine_train.arff')
df = pd.DataFrame(data[0])

k = 3
wine_results = []
while k < 8:
    print("\n")
    r = 1
    sum_d = 0
    for each in df.itertuples():
        #print(each)
        distances = []
        for row in df.itertuples():
            if each != row:
                add = 0
                for i in range(1, len(df.columns)-1):
                    add += math.pow(each[i]-row[i], 2)
                add = math.sqrt(add)
                distances.append([add, row[12]])
        distances.sort(key=lambda x: x[0])
        responses = []
        for p in range(k):
            responses.append(distances[p][1])
        mean = np.mean(responses)
        sum_d += abs(mean-each[12])
        print(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12]))
        s_values += str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12])+"\n"
        # file_wine.write(str(r)+" Predicted Value: " + str(mean) + "    Actual Value : " + str(each[12])+"\n")
        r += 1
    print_regression_result(sum_d/(r-1), r-1)
    wine_results.append([sum_d/(r-1), k])
    k += 2

file_wine.close()


data1 = arff.loadarff('yeast_train.arff')
df1 = pd.DataFrame(data1[0])

k = 3
while k < 8:
    print("\n")
    n = 1
    c = 0
    for each in df1.itertuples():
        #print(each)
        distances = []
        for row in df1.itertuples():
            if each != row:
                add = 0
                for i in range(1, len(df1.columns)-1):
                    add += math.pow(each[i]-row[i], 2)
                add = math.sqrt(add)
                distances.append([add, row[9]])
        distances.sort(key=lambda x: x[0])
        responses = []
        for p in range(k):
            responses.append(distances[p][1])
        mode = stats.mode(responses)
        if mode[0][0] == each[9]:
            c += 1
        print(str(n)+" Predicted Value: "+str(mode[0][0])+"    Actual Value : "+str(each[9]))
        file_yeast.write(str(n)+" Predicted Value: "+str(mode[0][0])+"    Actual Value : "+str(each[9])+"\n")
        n += 1
    print_class_result(c, n-1)
    k += 2
file_yeast.close()