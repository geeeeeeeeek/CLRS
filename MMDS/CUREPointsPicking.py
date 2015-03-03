__author__ = 'Tong'
# 5A3


def init_test_set():
    return [(0, 0), (10, 10)], [(1, 6), (3, 7), (4, 3), (7, 7), (8, 2), (9, 5)]


def distance(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


def points_picking():
    picked, unpicked = init_test_set()
    print(picked)
    while unpicked:
        max_distance = 0
        max_point = None
        for point in unpicked:
            min_distance = float("inf")
            for p in picked:
                if distance(p, point) < min_distance:
                    min_distance = distance(p, point)
            if min_distance > max_distance:
                max_distance = min_distance
                max_point = point
        picked.append(max_point)
        unpicked.remove(max_point)
        print(picked)

points_picking()