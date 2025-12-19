class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Initialize the result array.
        # res[i] will eventually hold the product of all elements except nums[i].
        res = [1] * n

        # -------------------------------
        # First loop: prefix products
        # -------------------------------
        # res[i] will store the product of all elements to the LEFT of index i.
        prefix = 1
        for i in range(n):
            # At index i, store the product of all previous elements
            res[i] = prefix
            
            # Update prefix to include nums[i] for the next index
            prefix *= nums[i]

        # -------------------------------
        # Second loop: suffix products
        # -------------------------------
        # Multiply into res[i] the product of all elements to the RIGHT of index i.
        suffix = 1
        for i in range(n - 1, -1, -1):
            # Multiply the existing prefix product with the suffix product
            res[i] *= suffix
            
            # Update suffix to include nums[i] for the next index to the left
            suffix *= nums[i]

        return res

        