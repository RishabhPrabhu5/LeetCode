class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)/2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            if nums[m] < target:
                l = m+1
        if nums[r] == target:
            return r
        return -1
        