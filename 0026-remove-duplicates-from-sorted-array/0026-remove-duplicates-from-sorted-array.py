class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]-1
        index = 0
        for i in range(len(nums)):
            if nums[i] != num:
                nums[index] = nums[i]
                index+=1
                num = nums[i]
        return index
        