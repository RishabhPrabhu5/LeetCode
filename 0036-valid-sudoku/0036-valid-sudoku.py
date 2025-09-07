class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {} #dict of sets
        columns = {}
        squares = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                elem = board[r][c]
                square_idx = c//3 + (r//3)*3
                if c == 0:
                    rows[r] = set()
                if r == 0:
                    columns[c] = set()
                if square_idx not in squares.keys():
                    squares[square_idx] = set()

                if elem in rows[r]:
                    return False
                elif elem != ".":
                    rows[r].add(elem)

                if elem in columns[c]:
                    return False
                elif elem != ".":
                    columns[c].add(elem)

                if elem in squares[square_idx]:
                    return False
                elif elem != ".":
                    squares[square_idx].add(elem)
        return True
                
        