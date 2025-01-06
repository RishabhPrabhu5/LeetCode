class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = defaultdict(list)
        for i in range(len(nums)):
            mp[nums[i]].append(i)
        
        for i in range(len(nums)):
            first = nums[i]
            if target-first in mp:
                if target-first == first:
                    if len(mp[target-first])>1:
                        return [i, mp[target-first][1]]
                else:
                    return [i, mp[target-first][0]]
        return [0,1]
