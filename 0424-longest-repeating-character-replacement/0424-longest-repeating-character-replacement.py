class Solution(object):
    def check_valid(self, dict, k):
        arr = dict.values()
        if len(arr) == 1:
            return True
        else:
            return sum(arr) - max(arr) <= k
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        max_f = 0
        max_len = 0
        seen_dict = defaultdict(int)
        
        for r in range(len(s)):
            # 1. Add the new character
            seen_dict[s[r]] += 1
            
            # 2. Update the maximum frequency found in the current window
            max_f = max(max_f, seen_dict[s[r]])
            
            # 3. Check validity: (Window size - Max Frequency)
            # If we have more than 'k' characters to replace, shrink from the left
            while (r - l + 1) - max_f > k:
                seen_dict[s[l]] -= 1
                l += 1
                # Note: Interestingly, max_f doesn't need to be decreased here. 
                # A smaller max_f would only make the window 'less' valid, 
                # so it won't help us find a new maximum length.
            
            # 4. Update the global max length
            max_len = max(max_len, r - l + 1)
            
        return max_len

        