__author__ = 'Tong'

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        m = num[0]
        for i in range(len(num)):
            if num[i] < num[i - 1]:
                m = min(m, num[i])
        return m