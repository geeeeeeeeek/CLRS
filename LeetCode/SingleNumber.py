__author__ = 'Tong'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for n in range(1, len(A))[::-1]:
            A[n - 1] ^= A[n]
        return A[0]


solution = Solution().singleNumber([1, 1, 2, 4, 2, 3, 4])
print(solution)
solution = Solution().singleNumber([1])
print(solution)