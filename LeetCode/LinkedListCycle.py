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
        while head and head.next:
            if head.val == head.next.val:
                return True
            head.next = head.next.next
            head = head.next
        return False


a = ListNode(3)
a.next = ListNode(2)
a.next.next = ListNode(0)
a.next.next.next = ListNode(-1)
a.next.next.next.next = a.next

print(Solution().hasCycle(a))
print(Solution().hasCycle(None))