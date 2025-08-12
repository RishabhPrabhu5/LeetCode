class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = 1
        r = n-1
        while l<r:
            if "0" in str(l) or "0" in str(r):
                l +=1
                r -=1
            else:
                break
        return [l,r]