__author__ = 'Tong'
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# click to show spoilers.
#
# Note:
# Your solution should be in logarithmic complexity.


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        num.append(float("-inf"))
        num.insert(0, float("-inf"))
        for i in range(1, len(num) - 1):
            if num[i] > num[i - 1] and num[i] > num[i + 1]:
                return i - 1