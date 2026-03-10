class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        while l < r:
            m = (l+r)//2
            time = sum((p + m - 1) // m for p in piles)
            if time <= h:
                r = m
            else:
                l = m+1
        return l

        