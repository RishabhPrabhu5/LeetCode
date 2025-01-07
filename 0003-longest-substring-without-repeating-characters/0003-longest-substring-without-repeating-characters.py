class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0]
        for start_index in range(len(s)):
            seen = set()
            count = 0
            for c in s[start_index:]:
                if c not in seen:
                    count += 1
                    seen.add(c)
                else:
                    counts.append(count)
                    break
            counts.append(count)
        return max(counts)
            
        