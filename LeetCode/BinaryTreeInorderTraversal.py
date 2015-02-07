__author__ = 'Tong'
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
# #    1
# #     \
# #      2
# #     /
# #    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        seq = []

        while root or stack:
            while root:
                stack.insert(0, root)
                root = root.left
            root = stack.pop(0)
            seq.append(root.val)
            root = root.right

        return seq


# r = TreeNode(1)
# r.right = TreeNode(2)
# r.right.left = TreeNode(3)
# print(Solution().inorderTraversal(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
print(Solution().inorderTraversal(r))