class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        prev_max = 0
        curr_max = nums[0]
        count = 1
        while curr_max < len(nums)-1:
            next_max = curr_max
            for i in range(prev_max, curr_max+1):
                if i+nums[i] > next_max:
                    p_m= i
                    next_max= i+nums[i]
            prev_max = p_m
            curr_max = next_max
            count +=1
        return count

            
        