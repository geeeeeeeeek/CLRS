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
        title = ""
        while num > 0:
            if num % 26 == 0:
                title = "Z" + title
                num = num // 26 - 1
            else:
                title = chr(num % 26 + 64) + title
                num //= 26
        return title


print(Solution().convertToTitle(28))