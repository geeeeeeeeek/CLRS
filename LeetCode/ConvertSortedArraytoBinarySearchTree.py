__author__ = 'Tong'
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node

    def sortedArrayToBST(self, num):
        if num is None or len(num) == 0:
            return
        mid = int(len(num) / 2)

        node = TreeNode(num[mid])
        if mid + 1 < len(num):
            node.right = self.sortedArrayToBST(num[mid + 1:])
        if mid > 0:
            node.left = self.sortedArrayToBST(num[:mid])
        return node


# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = [1]
t = Solution().sortedArrayToBST(n)
a = 1