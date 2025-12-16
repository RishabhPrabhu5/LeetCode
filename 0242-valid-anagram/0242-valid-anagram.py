class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        
        for i in range(len(t)):
            if countS.get(t[i], 0) == 0:
                return False
            else:
               countS[t[i]] -= 1 
        return True
        