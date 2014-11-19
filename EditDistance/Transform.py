__author__ = 'Tong'


def dpa(x, y):
    m = len(x)
    n = len(y)
    distance = [[0 for col in range(n + 1)] for row in range(m + 1)]
    for i in range(1, m + 1):
        distance[i][0] = i
    for j in range(1, n + 1):
        distance[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = distance[i - 1][j - 1]
            if x[i - 1] != y[j - 1]:
                diag += 1
            distance[i][j] = min(diag, distance[i - 1][j] + 1, distance[i][j - 1] + 1)
    print_trace(distance, m, n, x, y)
    print(distance[m][n])


def print_trace(distance, i, j, x, y):
    if i > 0 and j > 0:
        diag = distance[i - 1][j - 1]
        if x[i - 1] != y[j - 1]:
            diag += 1
        if distance[i][j] == diag:
            if x[i - 1] == y[j - 1]:
                print("None")
            else:
                print("replace")
            print_trace(distance, i - 1, j - 1, x, y)
        elif distance[i][j] == distance[i - 1][j] + 1:
            print("delete")
            print_trace(distance, i - 1, j, x, y)
        elif distance[i][j] == distance[i][j - 1] + 1:
            print("insert")
            print_trace(distance, i, j - 1, x, y)
    elif i > 0:
        if distance[i][j] == distance[i - 1][j] + 1:
            print("delete")
        print_trace(distance, i - 1, j, x, y)
    elif j > 0:
        if distance[i][j] == distance[i][j - 1] + 1:
            print("insert")
        print_trace(distance, i, j - 1, x, y)