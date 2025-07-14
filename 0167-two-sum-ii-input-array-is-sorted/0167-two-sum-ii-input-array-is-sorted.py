class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = len(numbers)-1
        l = 0
        while r>l:
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r] + numbers[l] < target:
                l +=1
            else:
                r-=1
        