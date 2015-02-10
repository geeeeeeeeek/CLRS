__author__ = 'Tong'
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution:
    # @return an integer
    def totalNQueens(self, n):
        if n == 0:
            return 0
        row = 0
        col = 0
        board = [-1] * n
        count = 0

        while True:
            if row == n:
                count += 1
                row -= 1
                while board[row] == n - 1:
                    if row == 0:
                        return count
                    board[row] = -1
                    row -= 1

                col = board[row] + 1
                board[row] = -1
                continue

            if self.canPlace(row, col, board):
                board[row] = col
                row += 1
                col = 0
            elif col == n - 1:
                board[row] = -1
                row -= 1

                while board[row] == n - 1:
                    if row == 0:
                        return count
                    board[row] = -1
                    row -= 1

                col = board[row] + 1
                board[row] = -1
            else:
                col += 1
        return count

    def canPlace(self, row, col, board):
        for i in range(len(board)):
            if i != row and board[i] != -1 and (col == board[i] or abs(board[i] - col) == abs(i - row)):
                return False
        return True


print(Solution().totalNQueens(0))