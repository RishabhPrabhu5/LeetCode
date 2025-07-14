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
            sum = numbers[r] + numbers[l]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l +=1
            else:
                r-=1
        