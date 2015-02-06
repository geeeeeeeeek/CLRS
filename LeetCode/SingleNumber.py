__author__ = 'Tong'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for n in A:
            result ^= n
        return result


solution = Solution().singleNumber([1, 1, 2, 4, 2, 3, 4])
print(solution)

solution = Solution().singleNumber([1])
print(solution)