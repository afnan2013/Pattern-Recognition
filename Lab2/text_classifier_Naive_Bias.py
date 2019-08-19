import math

# input of stop words from the file
f = open("stopwords.txt", "r")
stopword = f.read()
stop = []
stopwords_para = stopword.split("\n\n")
for i in stopwords_para:
    stopwords_line = i.split('\n')
    for j in stopwords_line:
        stopwords = j.split(" ")
        for k in stopwords:
            stop.append(k)
print(stop)
f.close()

# input of training sets from the file
train = open("corpus.txt", "r")
file = train.read()
paras = file.split("\n\n")

epsilon = 0.1
category = []
occurs = []
prob1 = []
words = []
selected = []
wordMatrix = [] # for the words appears in according to categories
prob2 = []


n = int(input("Please enter the number of Training Set, N : "))

for i in range(n):
    para = paras[i]
    lines = para.split("\n")

    if category.count(lines[1]) > 0:
        print(lines[1])
        for j in range(len(category)):
            if category[j] == lines[1]:
                occurs[j] = occurs[j]+1
    else:
        print(lines[1])
        category.append(lines[1])
        occurs.append(1)

    index = ""
    for cat in range(len(category)):
        if category[cat] == lines[1]:
            index = cat
            break
    currentParaWords = []
    for each in range(2, len(lines)):
        words = lines[each].split(" ")
        for each_word in words:
            each_word = each_word.lower()
            if (each_word[len(each_word) - 1] == ',' or each_word[len(each_word) - 1] == '.') and len(each_word)>2:
                each_word = each_word[:-1]
            if not stop.count(each_word) > 0 and len(each_word) > 2:
                row = [0, 0, 0, 0]
                if selected.count(each_word) > 0:
                    if currentParaWords.count(each_word) > 0:
                        print("It checks in "+str(i)+" "+each_word)
                    else:
                        indexOfWord = selected.index(each_word)
                        wordMatrix[indexOfWord][index] = wordMatrix[indexOfWord][index] + 1
                        currentParaWords.append(each_word)
                else:
                    selected.append(each_word)
                    row[index] = 1
                    wordMatrix.append(row)
                    currentParaWords.append(each_word)

for i in range(len(category)):
    p = (occurs[i]/n + epsilon)/(1 + len(category)*epsilon)
    p = -math.log(p, 2)
    prob1.append(p)


for i in range(len(selected)):
    row = []
    for j in range(len(occurs)):
        p = (wordMatrix[i][j] / occurs[j] + epsilon) / (1 + 2 * epsilon)
        p = -math.log(p, 2)
        row.append(p)
    prob2.append(row)

print(category)
print(occurs)
print(prob1)
print("\n\n")
print(selected)
print("\n\n")

for i in range(len(selected)):
    print(selected[i]+"  "+str(wordMatrix[i][0])+"  "+str(wordMatrix[i][1])+"  "+
          str(wordMatrix[i][2])+"  "+str(wordMatrix[i][3])+"   "+
          str(prob2[i][0])+"  "+str(prob2[i][1])+"  "+
          str(prob2[i][2])+"  "+str(prob2[i][3]))

print("\nItz time for testing\n")

print("The number of testing sets are :"+str(len(paras)-n))

for i in range(n, len(paras)):
    matchMatrix = []
    lines = paras[i].split("\n")
    print(lines[0])
    for line in lines:
        wordsTest = line.split(" ")
        for e in wordsTest:
            if selected.count(e) > 0:
                print(e, end=" ")
                indexOfMatch = selected.index(e)
                row = []
                for c in range(len(category)):
                    p = prob2[indexOfMatch][c]
                    row.append(p)
                matchMatrix.append(row)
    print(matchMatrix)
    sumProbabilities = []
    temp = []
    for c in range(len(prob1)):
        sumOfEachCategory = 0
        for each in matchMatrix:
            sumOfEachCategory += each[c]
        sumOfEachCategory += prob1[c]
        sumProbabilities.append(sumOfEachCategory)
    maxi = min(sumProbabilities)
    print(sumProbabilities)
    catIndex = 0
    for index2 in range(len(category)):
        if maxi == sumProbabilities[index2]:
            catIndex = index2
            break
    print(category[catIndex])

    print("\n")

