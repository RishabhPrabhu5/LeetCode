class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
    
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        
        while left < right:
            if height[left] < height[right]:
                # If current left height is a new max, update it
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Otherwise, it must be able to trap water
                    res += left_max - height[left]
                left += 1
            else:
                # If current right height is a new max, update it
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # Otherwise, it must be able to trap water
                    res += right_max - height[right]
                right -= 1
                
        return res
        