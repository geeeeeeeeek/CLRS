__author__ = 'Tong'
# Week 5 quiz 5B Q1
# Round 1 K - Means


class Cluster:
    centroid = None
    points = None

    def __init__(self, centroid):
        self.centroid = centroid
        self.points = []

    def __str__(self):
        p = "[Cluster] centroid : " + self.centroid.__str__() + "; points : "
        for point in self.points:
            p += point.__str__() + " "
        return p


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + self.x.__str__() + "," + self.y.__str__() + ")"

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


def distance(a, b):
    return pow(a.x - b.x, 2) + pow(a.y - b.y, 2)


def init_test_set():
    clusters = [Cluster(Point(25, 125)), Cluster(Point(44, 105)), Cluster(Point(29, 97)), Cluster(Point(35, 63)),
                Cluster(Point(55, 63)), Cluster(Point(42, 57)), Cluster(Point(23, 40)), Cluster(Point(64, 37)),
                Cluster(Point(33, 22)), Cluster(Point(55, 20))]
    points = [Point(28, 145), Point(65, 140), Point(50, 130), Point(38, 115), Point(55, 118), Point(50, 90),
              Point(43, 83), Point(63, 88), Point(50, 60), Point(50, 30)]
    return clusters, points


def k_means():
    clusters, points = init_test_set()

    # For each remaining point
    for point in points:
        # find the centroid to which point is closest
        opt_distance = float("inf")
        opt_cluster = None
        for cluster in clusters:
            if distance(point, cluster.centroid) < opt_distance:
                opt_distance = distance(point, cluster.centroid)
                opt_cluster = cluster
        # add point to the cluster if that centroid
        opt_cluster.points.append(point)

    print("++Points assigned.")
    for cluster in clusters:
        print(cluster)

    print("++Centroid adjusted.")
    # adjust the centroid of that cluster to account for point
    for cluster in clusters:
        temp = cluster.points.copy()
        temp.append(cluster.centroid)
        new_centroid = Point(0, 0)
        for t in temp:
            new_centroid.x += t.x
            new_centroid.y += t.y
        new_centroid.x /= len(temp)
        new_centroid.y /= len(temp)

        if not new_centroid.__eq__(cluster.centroid):
            cluster.points.append(cluster.centroid)
            cluster.centroid = new_centroid
        print(cluster)

    # reassign each point
    print("++Points reassigned.")
    for cluster in clusters:
        for point in cluster.points:
            # find the centroid to which point is closest
            opt_distance = float("inf")
            opt_cluster = None
            for c in clusters:
                if distance(point, c.centroid) < opt_distance:
                    opt_distance = distance(point, c.centroid)
                    opt_cluster = c
            if not cluster.centroid.__eq__(opt_cluster.centroid):
                print("Point " + point.__str__() + " is reassigned.")


k_means()