__author__ = 'Tong'
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
# #    1         3     3      2      1
# #     \       /     /      / \      \
# #      3     2     1      1   3      2
# #     /     /       \                 \
# #    2     1         2                 3


class Solution:
    # @return an integer
    def numTrees(self, n):
        g = [0] * (n + 1)
        g[0] = g[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                g[i] += g[j] * g[i - j - 1]
        return g[n]

# Explanation see the following link:
# https://oj.leetcode.com/discuss/24282/dp-solution-in-6-lines-with-explanation-f-i-g-i-1-g-n-i
# Generally speaking, suppose a node with value i, the left child ranges within 1..i - 1, and the right i+1..n.
# Then we can solve it as a DP problem. How could I didn't think of that!
print(Solution().numTrees(1))