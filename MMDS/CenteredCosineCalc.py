import math

__author__ = 'Tong'
b = [0, 3, 1, 2, 0]
d = [0, 4, 3, 0, 2]

ba = 0
da = 0
for i in range(0, 5):
    ba += b[i]
    da += d[i]

ba /= 5
da /= 5

aa = 0
bb = 0
cc = 0
for i in range(0, 5):
    aa += (b[i] - ba) * (d[i] - da)
    bb += math.pow((b[i] - ba), 2)
    cc += math.pow((d[i] - da), 2)

print(aa/math.sqrt(bb)/math.sqrt(cc))