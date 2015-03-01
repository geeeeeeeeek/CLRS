from math import sqrt
from pip.backwardcompat import raw_input

__author__ = 'Tong'
a = [0] * 6
for i in range(0, 6):
    a[i] = float(raw_input("a: "))
b = [0] * 6
for i in range(0, 6):
    b[i] = float(raw_input("b: "))
# c = [0] * 6
# for i in range(0, 6):
# a[i] = float(raw_input("c: "))

for alpha in range(3):
    print("alpha = " + alpha.__str__())
    # ab
    s = 0
    r = 0
    t = 0
    for i in range(5):
        s += a[i] * b[i]
        r += a[i] * a[i]
        t += b[i] * b[i]
    s += a[5] * b[5] * alpha * alpha
    # r += a[5] * a[5] * alpha * alpha
    # t += b[5] * b[5] * alpha * alpha
    print("AB : " + (s / sqrt(
        r * t + (a[5] * t + b[5] * r) * alpha * alpha + (
        a[5] * a[5] + b[5] * b[5]) * alpha * alpha * alpha * alpha)).__str__())