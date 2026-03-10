class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        best = r
        while l < r:
            m = (l+r)//2
            time = sum([math.ceil(float(x)/m) for x in piles])
            if time <= h:
                best = m
                r = m
            if time > h:
                l = m+1
        return best

        