class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        starts = set()
        for num in nums:
            if num-1 not in num_set:
                starts.add(num)
        
        max_len = 0
        for start in starts:
            curr = start
            count = 1
            while curr+1 in num_set:
                count +=1
                curr = curr+1
            max_len = max(count, max_len)
        return max_len

        