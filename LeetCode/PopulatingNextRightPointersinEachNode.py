__author__ = 'Tong'
# Given a binary tree
#
# #     struct TreeLinkNode {
# #       TreeLinkNode *left;
# #       TreeLinkNode *right;
# #       TreeLinkNode *next;
# #     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should
# be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two
# children).
# For example,
# Given the following perfect binary tree,
# #          1
# #        /  \
# #       2    3
# #      / \  / \
# #     4  5  6  7
# After calling your function, the tree should look like:
# #          1 -> NULL
# #        /  \
# #       2 -> 3 -> NULL
# #      / \  / \
# #     4->5->6->7 -> NULL


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        self.connect(left)
        self.connect(right)
        while left:
            left.next = right
            left = left.right
            right = right.left
        # return root


t = TreeNode(-1)
t.left = TreeNode(0)
t.right = TreeNode(1)
t.left.left = TreeNode(2)
t.left.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(5)
t.left.left.left = TreeNode(6)
t.left.right.left = TreeNode(8)
t.right.left.left = TreeNode(10)
t.right.right.left = TreeNode(12)
t.left.left.right = TreeNode(7)
t.left.right.right = TreeNode(9)
t.right.left.right = TreeNode(11)
t.right.right.right = TreeNode(13)

r1 = Solution().connect(t)
r2 = Solution().connect(None)
r3 = Solution().connect(t.right.right)

print("Test over.")