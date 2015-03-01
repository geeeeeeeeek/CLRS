__author__ = 'Tong'
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
# of the first two lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l = l1
            l1 = l1.next
        else:
            l = l2
            l2 = l2.next
        temp = l
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2
        return l

# print(Solution().mergeTwoLists(None, ListNode(1)))
# print(Solution().mergeTwoLists(ListNode(1), None))
# print(Solution().mergeTwoLists(ListNode(1), ListNode(1)))

a = ListNode(5)
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(4)
print(Solution().mergeTwoLists(a, b))