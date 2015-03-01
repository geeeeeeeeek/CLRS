from math import sqrt
from pip.backwardcompat import raw_input

__author__ = 'Tong'
a = float(raw_input("a: "))
b = float(raw_input("b: "))

print(a + b > 70)
print((a * a + b * b) > ((100 - a) * (100 - a) + (40 - b) * (40 - b)))