__author__ = 'Tong'
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        node = head
        while node and node.next:
            if node.val == node.next.val:
                return True
            node.next = node.next.next
            node = node.next
        return False


a = ListNode(3)
a.next = ListNode(2)
a.next.next = ListNode(0)
a.next.next.next = ListNode(-1)
a.next.next.next.next = a.next

print(Solution().hasCycle(a))
# print(Solution().hasCycle(None))