class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_idx = {}
        if len(s) < 2:
            return len(s)
        max_len = 1
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in last_idx and last_idx[c] >= start:
                #  print(start, i)
                max_len = max(max_len, i - start)
                start = last_idx[c]+1
            last_idx[c] = i
            # print(last_idx)
            
        max_len = max(max_len, i - start + 1)

        return max_len


                


            
        