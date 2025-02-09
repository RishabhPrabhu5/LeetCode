class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicates = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            diff = i - nums[i]
            count += duplicates[diff]
            duplicates[diff]+=1
        print(duplicates)

        return (len(nums) * (len(nums)-1))/2 - count

        