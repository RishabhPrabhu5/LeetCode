class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        l = 0
        r = k-1
        count = 0
        total = sum(arr[:k])
        while r < len(arr):
            if total >= k * threshold:
                count +=1
            total -= arr[l]
            l +=1
            r +=1
            if r == len(arr): break
            total += arr[r]
        return count


        