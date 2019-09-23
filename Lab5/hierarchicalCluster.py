import math
from scipy.cluster.hierarchy import linkage
n = int(input("Please input the train data row : "))

matrix = [[0 for i in range(n)] for j in range(n)]
X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]
Y = [[4, 4], [8, 4], [15, 8], [24, 4], [24, 12]]
print(X)
for i in range(n):
    v = input().split(" ")
    row = list(map(int, v))
    matrix.append(row)

print(linkage(Y, 'single', 'euclidean', False))

