class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k>len(s):
            return False
        mp = defaultdict(int)
        for l in s:
            mp[l]+=1
        odd_count = 0
        for l in mp:
            if mp[l]%2 == 1:
                odd_count+=1
        if odd_count > k:
            return False
        return True
        