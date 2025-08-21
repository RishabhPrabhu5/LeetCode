class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dfs_queue = []
        for c in range(len(board[0])):
            if board[0][c] == "O":
                dfs_queue.append((0,c))
            if board[len(board)-1][c] == "O":
                dfs_queue.append((len(board)-1,c))
        
        for r in range(len(board)):
            if board[r][0] == "O":
                dfs_queue.append((r,0))
            if board[r][len(board[0])-1] == "O":
                dfs_queue.append((r,len(board[0])-1))

        # print(dfs_queue)

        while len(dfs_queue) > 0:
            row, col = dfs_queue.pop(0)
            if board[row][col] == "O":
                board[row][col] = "S"
                if row >0 and board[row-1][col] == "O":
                    dfs_queue.append((row-1, col))
                if row < len(board)-1 and board[row+1][col] == "O":
                    dfs_queue.append((row+1, col))
                if col >0 and board[row][col-1] == "O":
                    dfs_queue.append((row, col-1))
                if col <len(board[0])-1 and board[row][col+1] == "O":
                    dfs_queue.append((row, col+1))

        # for r in range(len(board)):
        #     print(board[r])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "S":
                    board[r][c] = "O"
        # print()
        # for r in range(len(board)):
        #     print(board[r])


        