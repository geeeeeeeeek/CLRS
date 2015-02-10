__author__ = 'Tong'
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution:
    # @return an integer
    n = 0

    def totalNQueens(self, n):
        if n == 0:
            return 0
        self.n = n
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
        for i in range(self.n):
            if board[i] != -1 and i != row and (col == board[i] or abs(board[i] - col) == abs(i - row)):
                return False
        return True


for i in range(13):
    print("case " + i.__str__() + " : result = " + Solution().totalNQueens(i).__str__())