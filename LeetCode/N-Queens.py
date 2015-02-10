__author__ = 'Tong'
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
# a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
#
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]


class Solution:
    n = 0

    # @return a list of lists of string
    def solveNQueens(self, n):

        if n == 0:
            return []
        self.n = n
        row = 0
        col = 0
        board = [-1] * n
        result = []

        while True:
            if row == n:
                result.append(self.genResult(board))
                row -= 1
                while board[row] == n - 1:
                    if row == 0:
                        return result
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
                        return result
                    board[row] = -1
                    row -= 1

                col = board[row] + 1
                board[row] = -1
            else:
                col += 1
        return result

    def canPlace(self, row, col, board):
        for i in range(self.n):
            if board[i] != -1 and i != row and (col == board[i] or abs(board[i] - col) == abs(i - row)):
                return False
        return True

    def genResult(self, board):
        result = []
        for i in range(self.n):
            result.append('.' * board[i] + 'Q' + '.' * (self.n - board[i] - 1))
        return result


print(Solution().solveNQueens(8))