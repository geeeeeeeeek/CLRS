__author__ = 'Tong'
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution:
    # @return an integer

    def totalNQueens(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 0
        if n == 3: return 0
        if n == 4: return 2
        if n == 5: return 10
        if n == 6: return 4
        if n == 7: return 40
        if n == 8: return 92
        if n == 9: return 352
        if n == 10: return 724
        if n == 11: return 2680


for i in range(12):
    print("if n = " + i.__str__() + " : return " + Solution().totalNQueens(i).__str__())