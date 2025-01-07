class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        count = 0
        for start_index in range(len(s)):
            seen = set()
            count = 0
            for c in s[start_index:]:
                if c not in seen:
                    count += 1
                    seen.add(c)
                else:
                    # if count>max_len:
                    #     max_len = count
                    break
            if count>max_len:
                max_len = count
        return max_len
            
        