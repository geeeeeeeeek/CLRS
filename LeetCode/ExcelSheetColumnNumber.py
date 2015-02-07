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
        s = s[::-1]
        for i in range(len(s)):
            total += (ord(s[i]) - 64) * pow(26, i)
        return total


print(Solution().titleToNumber("AAA"))