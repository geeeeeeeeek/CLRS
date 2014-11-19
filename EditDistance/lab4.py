__author__ = 'Tong'


def test_stone(filename):
    file_handler = open(filename + '.in', 'a+', -1, "utf-8")
    file_handler.seek(0)
    x = file_handler.readline()[:-1]
    y = file_handler.readline()[:-1]
    file_handler.close()

    file_handler = open(filename + '.out', 'w', -1, "utf-8")
    ans = calc_distance(x, y)
    file_handler.write(ans.__str__() + "\n")
    file_handler.close()
    pass


# TODO You should implement a dynamic-programming algorithms and print the optimal operation sequence to the console.
def calc_distance(x, y):
    return 0


test_stone("lab4")