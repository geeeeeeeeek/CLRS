__author__ = 'Tong'
import random


class Element():
    key = 0
    index = 0

    def __init__(self, index, key):
        self.key = key
        self.index = index

    def __str__(self):
        return " (" + self.index.__str__() + ") : " + self.key.__str__()


def randomized_partition(a, p, r):
    i = p - 1
    for j in range(p, r):
        if a[j].key <= a[r].key:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[r], a[i + 1] = a[i + 1], a[r]
    return i + 1


def exchange_order(a, x, y, i):
    for ptr in range(x, y):
        if a[ptr].key == a[i].key and a[ptr].index > a[i].index:
            a[ptr], a[i] = a[i], a[ptr]
    return a


def stable_partition(a, p, r):
    i = p - 1
    for j in range(p, r):
        if a[j].key <= a[r].key:
            i += 1
            a[i], a[j] = a[j], a[i]
            a = exchange_order(a, p, i, i)
    i += 1
    a[r], a[i] = a[i], a[r]
    a = exchange_order(a, p, i, i)
    a = exchange_order(a, i + 1, r, i)
    return i


def insertion_sort(a):
    for j in range(len(a)):
        i = j - 1
        prior = a[j]
        while a[i].key > prior.key and i >= 0:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = prior
    return a


def quick_sort_randomized(a, p, r):
    if p < r:
        # Select a random prior.
        i = random.randint(p, r)
        a[i], a[r] = a[r], a[i]
        q = randomized_partition(a, p, r)

        quick_sort_randomized(a, p, q - 1)
        quick_sort_randomized(a, q + 1, r)
    return a


def quick_sort_stable(a, p, r):
    if p < r:
        # Select a random prior.
        i = random.randint(p, r)
        a[i], a[r] = a[r], a[i]
        q = stable_partition(a, p, r)

        quick_sort_stable(a, p, q - 1)
        quick_sort_stable(a, q + 1, r)
    return a


def quick_sort_mixed(a, p, r):
    if p < r:
        # Select a random prior.
        i = random.randint(p, r)
        a[i], a[r] = a[r], a[i]
        q = stable_partition(a, p, r)

        if q - p > 10:
            a = quick_sort_stable(a, p, q - 1)
        else:
            a = a[:p] + insertion_sort(a[p:q - 1 + 1]) + a[q:]
        if r - q > 10:
            a = quick_sort_stable(a, q + 1, r)
        else:
            a = a[:q + 1] + insertion_sort(a[q + 1: r + 1]) + a[r + 1:]
    return a


# ##################################################### #
# #                      Test Cases                   # #
# ##################################################### #


def is_correct(a):
    result = ""
    for index in range(len(a) - 1):
        if a[index].key > a[index + 1].key:
            result += "ERROR: SORT MISTAKE at " + a[index].__str__() + ", " + a[index + 1].__str__() + "\n"
    if result == "":
        result += "Completely correct!"
    return result


def is_stable(a):
    result = ""
    for index in range(len(a) - 1):
        if a[index].key > a[index + 1].key:
            result += "ERROR: SORT MISTAKE at " + a[index].__str__() + ", " + a[index + 1].__str__() + "\n"
        if a[index].key == a[index + 1].key and a[index].index > a[index + 1].index:
            result += "ERROR: ORDER MISTAKE at " + a[index].__str__() + ", " + a[index + 1].__str__() + "\n"
    if result == "":
        result += "Completely correct!"
    return result


def construct_test_cases(elements):
    test_set = []
    for index in range(len(elements)):
        case = Element(index, elements[index])
        test_set.append(case)
    return test_set


def construct_test_random():
    test_set = []
    for index in range(100):
        case = Element(index, int(random.random() * 100))
        test_set.append(case)
    return test_set


def test(elements, func):
    print("> Test begin:")

    result = func(elements, 0, len(elements) - 1)
    output(result)
    if func == quick_sort_stable:
        print(is_stable(result))
    else:
        print(is_correct(result))


def output(a):
    for each in a:
        print(each)


print("\n" + "> Randomized quick sort:")
test_cases_0 = construct_test_cases([8, 5, 6, 4, 2])
test_cases_1 = construct_test_cases([1, 7, 4, 6, 3, 9, 15])
test_cases_2 = construct_test_cases([4, 2, 52, 5, 69, 8, 56, 58, 7, 6])
test(test_cases_0, quick_sort_randomized)
test(test_cases_1, quick_sort_randomized)
test(test_cases_2, quick_sort_randomized)

print("\n" + "> Stable quick sort:")
test_cases_3 = construct_test_cases([8, 5, 6, 8, 4])
test_cases_4 = construct_test_cases([4, 2, 52, 2, 69, 8, 26, 38, 7, 6])
test_cases_5 = construct_test_cases([1, 7, 7, 6, 6, 4, 6, 8, 8, 9])
test(test_cases_3, quick_sort_stable)
test(test_cases_4, quick_sort_stable)
test(test_cases_5, quick_sort_stable)

print("\n" + "> Mixed quick sort:")
test_cases_random = construct_test_random()
test(test_cases_random, quick_sort_mixed)