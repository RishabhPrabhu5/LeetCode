class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixes = [1]
        suffixes = [1]
        forward = 1
        backward = 1
        for i in range(len(nums)-1):
            forward *= nums[i]
            backward *= nums[len(nums)-1-i]
            prefixes.append(forward)
            suffixes.append(backward)

        ret = []
        for i in range(len(prefixes)):
            ret.append(prefixes[i] * suffixes[len(suffixes)-1-i])
        return ret

        