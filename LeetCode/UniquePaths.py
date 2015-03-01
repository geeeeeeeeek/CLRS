__author__ = 'Tong'

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.


class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        d = [[0] * n] * m
        for i in range(n):
            d[0][i] = 1
        for i in range(m):
            d[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i][j - 1] + d[i - 1][j]
        return d[m - 1][n - 1]


print(Solution().uniquePaths(2, 3))