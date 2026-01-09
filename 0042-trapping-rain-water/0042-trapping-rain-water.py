class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        max_left = [0] * n
        max_right = [0] * n
        
        curr_l = 0
        curr_r = 0
        
        # Single pass to fill both boundary arrays
        for i in range(n):
            # Left-to-right logic
            h_l = height[i]
            if h_l > curr_l:
                curr_l = h_l
            max_left[i] = curr_l
            
            # Right-to-left logic (using negative indexing)
            # i=0 fills the last index, i=1 fills second to last, etc.
            r_idx = n - 1 - i
            h_r = height[r_idx]
            if h_r > curr_r:
                curr_r = h_r
            max_right[r_idx] = curr_r

        # Final calculation pass
        ret = 0
        for i in range(n):
            # Optimized min(max_left[i], max_right[i])
            ml, mr = max_left[i], max_right[i]
            lower_wall = ml if ml < mr else mr
            
            # Optimized max(lower_wall - height[i], 0)
            diff = lower_wall - height[i]
            if diff > 0:
                ret += diff
                
        return ret
            