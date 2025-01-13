class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = ["I","V","X","L","C","D","M"]
        vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500, "M":1000}
        arr = []
        prev = s[0]
        ans = 0
        count = 1
        for i in range(1,len(s)):
            curr = s[i]
            if prev != curr:
                if numerals.index(prev) < numerals.index(curr):
                    ans -= count * vals[prev]
                else:
                    ans += count * vals[prev]
                count = 1
                prev = curr
            else:
                count +=1
        ans += count * vals[prev]
        return ans