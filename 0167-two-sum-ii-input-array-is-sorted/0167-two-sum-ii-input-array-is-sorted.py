class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = 0, len(numbers)-1
        while a < b:
            sums = numbers[a] + numbers[b]
            if sums == target:
                return [a+1, b+1]
            elif sums > target:
                b -= 1
            else:
                a += 1
        return []
        