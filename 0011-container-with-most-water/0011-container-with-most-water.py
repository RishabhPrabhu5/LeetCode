class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) -1
        m = 0
        while r>l:
            val = (r-l) * min(height[l], height[r])
            if val > m:
                m = val
            if height[r]>height[l]:
                l +=1
            else:
                r -=1
        return m

        
        