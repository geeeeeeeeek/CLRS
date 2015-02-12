__author__ = 'Tong'
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return
        last = head
        current = last.next
        while current:
            if current.val == last.val:
                last.next = current.next
            else:
                last = current
            current = current.next
        return head


h = ListNode(1)
h.next = ListNode(1)
h.next.next = ListNode(1)
# h.next.next.next = ListNode(3)
# h.next.next.next.next = ListNode(3)
print(Solution().deleteDuplicates(h))