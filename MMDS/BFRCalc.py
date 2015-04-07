__author__ = 'Tong'
import math

n = 1000
s = [-323, 1066, 1776]
ss = [412, 1500, 3500]

sd = [0, 0, 0]
cen = [0, 0, 0]

total = 0

for i in range(0, 3):
    sd[i] = ss[i] / n - math.pow((s[i] / n), 2)
    cen[i] = s[i] / n
    total += (math.pow(cen[i], 2) / sd[i])

print(math.sqrt(total))