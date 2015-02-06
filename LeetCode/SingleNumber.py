__author__ = 'Tong'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for n in A:
            result ^= n
        return result

# Explanation of the algorithm #
# Since the result of 'xor' two same numbers is 0,
# 'xor' each element and we get the only single number.

solution = Solution().singleNumber([1, 1, 2, 4, 2, 3, 4])
print(solution)

solution = Solution().singleNumber([1])
print(solution)