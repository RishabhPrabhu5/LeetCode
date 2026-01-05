class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min = 10000
        max = 0
        profit = 0
        for price in prices:
            if price< min:
                min = price
                max = 0
            if price>max:
                max = price
            if max - min > profit:
                    profit = max-min

        return 0 if profit <0 else profit

            