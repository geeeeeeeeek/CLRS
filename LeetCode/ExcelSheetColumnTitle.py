__author__ = 'Tong'
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB


class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num <= 26:
            return chr(num + 64)
        if num % 26 == 0:
            return self.convertToTitle(int(num / 26) - 1) + "Z"
        return self.convertToTitle(int(num / 26)) + chr(num % 26 + 64)


print(Solution().convertToTitle(52))