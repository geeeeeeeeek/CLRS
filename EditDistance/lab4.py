from EditDistance.Transform import dpa

__author__ = 'Tong'


def test_stone(filename):
    file_handler = open(filename + '.in', 'a+', -1, "utf-8")
    file_handler.seek(0)
    num = 4
    s = []
    for i in range(num):
        s.append(file_handler.readline()[:-1])
    file_handler.close()

    file_handler = open(filename + '.out', 'w', -1, "utf-8")
    for i in range(num):
        for j in range(i + 1, num):
            ans = dpa(s[i], s[j])
            file_handler.write(s[i] + " and " + s[j] + " : "+ "\n")
    file_handler.close()


# TODO You should implement a dynamic-programming algorithms and print the optimal operation sequence to the console.
def calc_distance(x, y):
    dpa(x, y)
    return 0


test_stone("lab4")