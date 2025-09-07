class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]  # 3x3 boxes

        for r in range(9):
            for c in range(9):
                elem = board[r][c]
                if elem == ".":
                    continue

                square_idx = (r // 3) * 3 + (c // 3)

                if elem in rows[r] or elem in columns[c] or elem in squares[square_idx]:
                    return False

                rows[r].add(elem)
                columns[c].add(elem)
                squares[square_idx].add(elem)

        return True

                
        