__author__ = 'Tong'
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution:
    # @return an integer
    n = 0
    count = 0

    def totalNQueens(self, n):
        self.n = n
        self.queen(0, [-1] * n)
        return self.count

    def queen(self, row, board):
        if row == self.n:
            self.count += 1
            return
        for c in range(self.n):
            if self.canPlace(row, c, board):
                board[row] = c
                self.queen(row + 1, board)
            board[row] = -1

    def canPlace(self, row, col, board):
        for i in range(self.n):
            if i != row and board[i] != -1 and (col == board[i] or abs(board[i] - col) == abs(i - row)):
                return False
        return True


print(Solution().totalNQueens(0))