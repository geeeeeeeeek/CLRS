__author__ = 'Tong'
import math


class Heap():
    __a = []
    __d = 2
    __size = 0

    def __init__(self, a, d):
        self.__a = a
        self.__d = d

    def build(self):
        self.__size = len(self.__a) - 1
        for i in range(1, math.floor(self.__size / 2) + 1)[::-1]:
            self.max_heapify(i)
        return 0

    def max_heapify(self, i):
        children = self.__get_children(i)
        if not children:
            return
        largest_index = i
        for child in children:
            if self.__a[child] > self.__a[largest_index]:
                largest_index = child
        if largest_index != i:
            self.__a[i], self.__a[largest_index] = self.__a[largest_index], self.__a[i]
            self.max_heapify(largest_index)

    def sort(self):
        self.build()
        for i in range(2, len(self.__a))[::-1]:
            self.__a[1], self.__a[i] = self.__a[i], self.__a[1]
            self.__size -= 1
            self.max_heapify(1)

    def __get_children(self, i):
        left = self.__d * (i - 1) + 2
        right = self.__d * i + 1
        if left > self.__size:
            return []
        if right > self.__size:
            return [t for t in range(left, self.__size + 1)]
        return [t for t in range(left, right + 1)]

    def __get_parent(self, i):
        return math.trunc((i + self.__d - 2) / self.__d)

    def insert(self, k):
        self.__size += 1
        self.__a.append(float("-inf"))
        self.increase_key(self.__size, k)

    def increase_key(self, i, k):
        self.__a[i] = k if self.__a[i] < k else self.__a[i]
        while i > 1 and self.__a[self.__get_parent(i)] < self.__a[i]:
            self.__a[i], self.__a[self.__get_parent(i)] = self.__a[self.__get_parent(i)], self.__a[i]
            i = self.__get_parent(i)

    def extract_max(self):
        max__ = self.__a[1]
        self.__a[1] = self.__a[self.__size]
        self.__a.pop()
        self.__size -= 1
        self.max_heapify(1)
        return max__

    def __str__(self):
        return self.__a[1:]

# ##################################################### #
# #                      Test Cases                   # #
# ##################################################### #

# 2 - arg
test_cases_1 = [None, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_sort(test_cases, d):
    heap = Heap(test_cases_1, d)
    heap.sort()
    print(heap.__str__())


def test_insert(test_cases, d, k):
    heap = Heap(test_cases_1, d)
    heap.build()
    heap.insert(k)
    print(heap.__str__())


def test_extract_max(test_cases, d):
    heap = Heap(test_cases_1, d)
    heap.build()
    max_ = heap.extract_max()
    print(max_)
    print(heap.__str__())


def test_increase_key(test_cases, d, i, k):
    heap = Heap(test_cases_1, d)
    heap.build()
    heap.increase_key(i, k)
    print(heap.__str__())


test_extract_max(test_cases_1, 2)