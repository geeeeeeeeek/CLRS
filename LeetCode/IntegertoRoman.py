__author__ = 'Tong'
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @return a string
    def intToRoman(self, num):
        # d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = self.resolver("M", "M", "M", num // 1000)
        num %= 1000
        result += self.resolver("C", "D", "M", num // 100)
        num %= 100
        result += self.resolver("X", "L", "C", num // 10)
        num %= 10
        result += self.resolver("I", "V", "X", num)
        return result

    def resolver(self, one, five, ten, num):
        if num <= 3:
            return one * num
        elif num <= 5:
            return one * (5 - num) + five
        elif num <= 8:
            return five + one * (num - 5)
        else:
            return one * (10 - num) + ten


print(Solution().intToRoman(39))