__author__ = 'Tong'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        i = 0
        while i < (len(A) - 1) / 2:
            A[len(A) - i - 2] ^= A[len(A) - 1 - i]
            A[i + 1] ^= A[i]

            i += 1
        return A[int((len(A) - 1) / 2)]


solution = Solution().singleNumber([1, 1, 2, 4, 2, 3, 4])
print(solution)

solution = Solution().singleNumber([1])
print(solution)