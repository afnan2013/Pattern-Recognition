n = int(input("Please input the train data row : "))


def cluster_merge(oldCluster, i, j):  # i is the index for merging and j is the index of merging value
    row = oldCluster[i]
    for k in range(len(oldCluster[j])):
        row.append(oldCluster[j][k])
    oldCluster.remove(oldCluster[j])
    return oldCluster


def solve(cluster, samples):
    total = []
    for i in range(len(cluster)-1):
        for j in range(len(cluster)-1):
            if i !=j:
                c1 = cluster_merge(cluster, i, j)
                total.append(c1)
                break
    print(total)


trainSet = [[4, 4], [8, 4], [15, 8], [20, 6], [21, 10],[24, 4], [24, 12]]
cluster = [[i] for i in range(n)]
solve(cluster, trainSet)

