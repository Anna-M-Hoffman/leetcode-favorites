# N-QUEENS
# The n-queens puzzle is the problem of placing n queens 
# on an n x n chessboard so that no two queens can attack each other.

# Each solution contains a unique board layout where the queen pieces
#  are placed. 'Q' indicates a queen and '.' indicates an empty space.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Positive diagonal (r + c)
        # Negative diagonal (r - c)
        # Iterate through rows, with no column overlap between queens

        res = []
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # Base case - the end of the row is reached
            if r == n:
                curRow = ["".join(row) for row in board]
                res.append(curRow)
                return

            for c in range(n): # Which column does the queen go?

                # Conditions where Q cannot be added
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                # Q can be added
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1) # Go through another row

                # Undo additions
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res

