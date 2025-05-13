class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        seen = set()
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] <0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j], nums[k]) not in seen:
                        ret.append([nums[i], nums[j], nums[k]])
                        seen.add((nums[i], nums[j], nums[k]))
                    k-=1
                else: k-=1
        return ret

        