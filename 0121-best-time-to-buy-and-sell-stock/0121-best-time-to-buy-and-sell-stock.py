class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_seen = 10000
        m = 0
        for i in range(len(prices)):
            min_seen = min(min_seen, prices[i])
            curr = prices[i] - min_seen
            m = max(m, curr)
        return m

            