class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        i = 0
        j = 0
        direction = 0 if n > 1 else 1
        visited = set()
        while len(ret) < len(matrix) * len(matrix[0]):
            visited.add((i,j))
            ret.append(matrix[i][j])
            if direction == 0:
                j +=1
                if j >= n-1 or (i,j+1) in visited:
                    direction = 1
            elif direction == 1:
                i +=1
                if i >= m-1 or (i+1,j) in visited:
                    direction = 2
            elif direction == 2:
                j -=1
                if j <= 0 or (i,j-1) in visited:
                    direction = 3
            else:
                i -=1
                if i <= 0 or (i-1,j) in visited:
                    direction = 0
        return ret
            
            

