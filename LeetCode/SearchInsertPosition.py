__author__ = 'Tong'
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where
# it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return 0
        return self.binarySearch(0, len(A), A, target)

    def binarySearch(self, p, q, A, target):
        mid = (p + q) // 2
        if q - p == 1:
            return p if A[p] >= target else q
        return self.binarySearch(p, mid, A, target) if target < A[mid] else self.binarySearch(mid, q, A, target)


print(Solution().searchInsert([1, 3, 4], 2))