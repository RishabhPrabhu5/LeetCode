class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = 1, len(numbers)
        while a < b:
            sums = numbers[a-1] + numbers[b-1]
            if sums == target:
                return [a, b]
            elif sums > target:
                b -= 1
            else:
                a += 1
        return []
        