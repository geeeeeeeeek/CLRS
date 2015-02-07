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
        if len(s) == 1:
            return ord(s) - 64
        return ord(s[-1]) - 64 + self.titleToNumber(s[:-1]) * 26


print(Solution().titleToNumber("AB"))