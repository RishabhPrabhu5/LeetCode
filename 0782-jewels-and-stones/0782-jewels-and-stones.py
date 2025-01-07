class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        mp = defaultdict(int)
        for c in stones:
            mp[c]+=1
        count = 0
        for l in jewels:
            count += mp[l]
        return count
        