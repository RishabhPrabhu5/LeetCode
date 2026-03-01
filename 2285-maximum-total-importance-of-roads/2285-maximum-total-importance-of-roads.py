import numpy as np

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degrees = [0]*n
        for [a,b] in roads:
            degrees[a] +=1
            degrees[b] +=1
        
        sort = sorted(degrees)
        print(sort)

        s = 0
        for i in range(n):
            s += (i+1) * sort[i]

        return s

            
        