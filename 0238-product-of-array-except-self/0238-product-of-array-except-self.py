class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forward = [1]
        for i in range(1, len(nums)):
            forward.append(forward[-1] * nums[i-1])
        
        backward = [1]
        for i in range(len(nums)-1, 0, -1):
            backward.insert(0, backward[0] * nums[i])
    
        # print(forward, backward)
        ret = []    
        for i in range(len(forward)):
            ret.append(forward[i] * backward[i])
        return ret
        