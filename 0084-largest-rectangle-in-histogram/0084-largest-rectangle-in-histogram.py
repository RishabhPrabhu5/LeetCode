class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = [] #height, leftmost index for that height
        n = len(heights)

        for i in range(n):
            curr_height = heights[i]
            popped = False
            while stack and curr_height < stack[-1][0]:
                popped = True
                h, s_idx = stack.pop()
                if (i-s_idx) * h > max_area:
                    max_area = (i-s_idx) * h
                
            if popped:
                stack.append((curr_height, s_idx))
            else:
                stack.append((curr_height, i))
        
        while stack:
            h, s_idx = stack.pop()
            if (n-s_idx) * h > max_area:
                max_area = (n-s_idx) * h

        return max_area

                


        