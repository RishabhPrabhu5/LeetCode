class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = defaultdict(int)
        for num in nums:
            mp[num] +=1
        arr = mp.keys()

        dp = {}
        dp[0] = arr[0] * mp[arr[0]]
        if len(arr) < 2:
            return dp[0]

        if arr[0] < arr[1] -1:
            dp[1] = dp[0] + arr[1]*mp[arr[1]]
        else:
            dp[1] = max(arr[0] * mp[arr[0]], arr[1] * mp[arr[1]])


        for i in range(2, len(arr)):
            if arr[i-1] < arr[i] -1:
                dp[i] = dp[i-1] + arr[i]*mp[arr[i]]
            else:
                dp[i] = max(arr[i]*mp[arr[i]] + dp[i-2], dp[i-1])
        print(dp)

        return dp[len(arr)-1]
 
        
