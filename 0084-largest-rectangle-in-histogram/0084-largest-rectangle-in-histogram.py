class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = [] #height, leftmost index for that height

        for i in range(len(heights)):
            curr_height = heights[i]
            popped = False
            while stack and curr_height < stack[-1][0]:
                popped = True
                h, s_idx = stack.pop()
                if (i-s_idx) * h > max_area:
                    max_area = (i-s_idx) * h
                
                # print(i, max_area)
            if popped:
                stack.append((curr_height, s_idx))
            else:
                stack.append((curr_height, i))
            # print(stack)
        
        while stack:
            h, s_idx = stack.pop()
            if (len(heights)-s_idx) * h > max_area:
                max_area = (len(heights)-s_idx) * h

        return max_area

                


        