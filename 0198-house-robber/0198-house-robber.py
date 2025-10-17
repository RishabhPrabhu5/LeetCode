class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = nums[1]
        max_seen_prev = nums[0]
        
        for i in range(2, n):
            max_seen_prev = max(max_seen_prev, dp[i-2])
            #logic to get next elem
            dp[i] = nums[i] + max_seen_prev
        
        return max(dp[-1], dp[-2])