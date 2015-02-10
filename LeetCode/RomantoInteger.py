__author__ = 'Tong'
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @return an integer
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last = 0
        value = 0
        for i in s:
            if d[i] <= last:
                value += d[i]
            else:
                value += d[i]
                value -= last * 2
            last = d[i]
        return value

# This problem is too tricky. It's a waste of time.
print(Solution().romanToInt("MMMCMXCIX"))