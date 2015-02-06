__author__ = 'Tong'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        n = len(A) - 1
        while 0 < n:
            A[n - 1] ^= A[n]
            n -= 1
        return A[0]


solution = Solution().singleNumber([1, 1, 2, 4, 2, 3, 4])
print(solution)