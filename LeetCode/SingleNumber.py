__author__ = 'Tong'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d = {}
        for a in A:
            if not d.get(a):
                d[a] = True
            else:
                d.pop(a)
        for key in d.keys():
            return key


solution = Solution().singleNumber([1, 2, 3, 3, 2, 1, 4])
print(solution)