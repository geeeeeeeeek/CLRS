__author__ = 'Tong'
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
# #    A -> 1
# #     B -> 2
# #     C -> 3
# #     ...
# #    Z -> 26
# #   AA -> 27
# #  AB -> 28


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        total = 0
        l = len(s)
        for i in range(l):
            total += (ord(s[l - i - 1]) - 64) * pow(26, i)
        return total


print(Solution().titleToNumber("A"))