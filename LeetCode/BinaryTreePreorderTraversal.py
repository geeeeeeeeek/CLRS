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
# return [1,2,3].
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
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        seq = []
        while stack:
            node = stack.pop(0)
            seq.append(node.val)
            if node.right:
                stack.insert(0, node.right)
            if node.left:
                stack.insert(0, node.left)
        return seq


r = TreeNode(1)
# r.right = TreeNode(2)
# r.right.left = TreeNode(3)
print(Solution().preorderTraversal(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
print(Solution().preorderTraversal(r))