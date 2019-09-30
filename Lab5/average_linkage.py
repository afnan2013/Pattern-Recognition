import math
import numpy as np

n = int(input("Please input the train data row : "))


def print_distance_matrix(m, l):
    for i in range(l):
        for j in range(l):
            print(m[i][j], end=" ")
        print("")


def print_cluster(c):
    for i in range(len(c)):
        r = c[i]
        r.sort()
    print(c)


def cluster_merge(oldCluster, i, j):  # i is the index for merging and j is the index of merging value
    row = oldCluster[i]
    for k in range(len(oldCluster[j])):
        row.append(oldCluster[j][k])
    oldCluster.remove(oldCluster[j])
    return oldCluster


def first_distance_matrix(cluster, s):
    m = [[10000 for p in range(n)] for q in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                d = (s[i][0] - s[j][0]) * (s[i][0] - s[j][0]) + (s[i][1] - s[j][1]) * (s[i][1] - s[j][1])
                m[i][j] = math.sqrt(d)
    return m


def distance_matrix(cluster, fisrtDistanceMatrix):
    m = [[10000 for p in range(len(cluster))] for q in range(len(cluster))]
    for i in range(len(cluster)):
        for j in range(i):
            if i != j:
                temp = []
                for p in range(len(cluster[i])):
                    for q in range(len(cluster[j])):
                        p1 = cluster[i][p]
                        p2 = cluster[j][q]
                        temp.append(fisrtDistanceMatrix[p1][p2])
                m[i][j] = np.average(temp)
    return m


def find_smallest_value_index(d_matrix):
    mini = 10000
    temp_i = 0
    temp_j = 0
    for i in range(len(d_matrix)):
        for j in range(len(d_matrix)):
            if d_matrix[i][j] < mini:
                mini = d_matrix[i][j]
                temp_i = i
                temp_j = j
    return [temp_i, temp_j]


def solve(cluster, train):
    first = first_distance_matrix(cluster, train)
    print_cluster(cluster)
    print_distance_matrix(first, n)
    s_index = find_smallest_value_index(first)
    print("The smallest value in this level - ", np.min(first))
    while 1:
        if len(cluster) <= 2:
            break
        cluster = cluster_merge(cluster, s_index[0], s_index[1])
        print_cluster(cluster)
        dm = distance_matrix(cluster, first)
        #print_distance_matrix(dm, len(dm))
        print("The smallest value in this level - ", np.min(dm))
        s_index = find_smallest_value_index(dm)
    print(cluster_merge(cluster, 0, 1))

trainSet = [[4, 4], [8, 4], [15, 8], [20, 6], [21, 10],[24, 4], [24, 12]]
cluster = [[i] for i in range(n)]

solve(cluster, trainSet)




