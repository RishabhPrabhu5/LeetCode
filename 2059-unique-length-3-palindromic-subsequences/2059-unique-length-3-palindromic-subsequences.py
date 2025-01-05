class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        pals = set()
        right = len(s)-1
        seen = {}
        parsed = set()
        for i in range(len(s)-2):
            if s[i] in parsed:
                continue
            parsed.add(s[i])
            
            if s[i] in seen:
                last = seen[s[i]]
            else:
                while s[right]!= s[i] and right >= i+2:
                    if s[right] not in seen:
                        seen[s[right]] = right
                    right -=1
                last = right
            
            for l in set(s[i+1:last]):
                pals.add(s[i]+l+s[last])
                if len(pals) >= 676:
                    return 676


        return(len(pals))


        