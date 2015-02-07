__author__ = 'Tong'
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif (not p) ^ (not q):
            return False

        if p.val != q.val or (not not p.left) ^ (not not q.left) or (not not p.right) ^ (not not q.right):
            return False

        if p.left and q.left and not self.isSameTree(p.left, q.left):
            return False

        if p.right and q.right and not self.isSameTree(p.right, q.right):
            return False

        return True


a = TreeNode(1)
b = TreeNode(1)
a.left = TreeNode(2)
b.left = TreeNode(2)
print(Solution().isSameTree(a, b))