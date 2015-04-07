__author__ = 'Tong'

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
# then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        j = 0
        for i in range(len(A)):
            if A[j] == 0:
                A.insert(0, A.pop(j))
            elif A[j] == 2:
                A.append(A.pop(j))
                j -= 1
            j += 1
        # print(A)


Solution().sortColors([1, 2, 0, 1, 2, 0])