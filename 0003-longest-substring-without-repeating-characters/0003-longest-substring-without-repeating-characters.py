class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        l, r = 0, 0
        seen = {s[l], s[r]}
        max = 0
        while r < len(s)-1:
            while s[r+1] in seen:
                seen.remove(s[l])
                l+=1
            r +=1
            seen.add(s[r])
            if r-l+1 > max:
                max = r-l+1
                print(r, l)
        return max


                


            
        