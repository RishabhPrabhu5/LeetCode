class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=max(nums)
        if i< 0:
            return i
        left = tot = curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr < 0:
                curr -= nums[left]
                left+=1
            tot = max(tot, curr)
        return tot
        