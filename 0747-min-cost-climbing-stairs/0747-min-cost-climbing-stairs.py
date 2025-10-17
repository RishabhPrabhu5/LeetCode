class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost)+1)
        dp[1] = cost[0]
        dp[2] = min(cost[0], cost[1])
        if len(cost) < 3:
            return dp[len(cost)]
        dp[3] = min(cost[2] + dp[2], cost[1])
        for i in range(4, len(cost) +1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        return dp[len(cost)]

        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] += min(cost[i + 1], cost[i + 2])

        # return min(cost[0], cost[1])
        
            