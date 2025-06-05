class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            matrix[i] = [0] * len(matrix[0])

        for i in range(len(matrix)):
            if i not in zero_rows:
                for j in zero_cols:
                    matrix[i][j] = 0
        
        