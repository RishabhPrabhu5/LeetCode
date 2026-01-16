class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        m, n = len(s), len(t)
        if n > m:
            return ""

        target = Counter(t)
        curr = Counter(t)          # counts still needed
        remaining = n              # total characters still needed
        length = 0
        min_len = m + 1
        best_l = 0

        l = r = 0
        while r < m:
            # Add character on the right
            right_char = s[r]
            if right_char in target:
                if curr[right_char] > 0:
                    remaining -= 1
                curr[right_char] -= 1

            length += 1

            # Try shrinking from the left while valid
            while remaining == 0:
                if length < min_len:
                    min_len = length
                    best_l = l

                left_char = s[l]
                if left_char in target:
                    curr[left_char] += 1
                    if curr[left_char] > 0:
                        remaining += 1

                l += 1
                length -= 1

            r += 1

        return "" if min_len == m + 1 else s[best_l:best_l + min_len]



        