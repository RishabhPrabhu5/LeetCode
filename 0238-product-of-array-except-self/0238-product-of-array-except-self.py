class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n  # Output array

        # Compute prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix          # Product of elements to the left
            prefix *= nums[i]        # Update prefix

        # Compute suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix         # Multiply by right-side product
            suffix *= nums[i]        # Update suffix

        return res

        