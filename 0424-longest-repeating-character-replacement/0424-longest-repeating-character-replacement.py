class Solution(object):
    def check_valid(self, dict, k):
        sorted_arr = sorted(dict.values())
        if len(sorted_arr) == 1:
            return True
        else:
            return sum(sorted_arr[:-1]) <= k
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # v1 = {"B":2, "C":1}
        # i1 = {"A":2, "B":2}
        # print(self.check_valid(v1, 1))
        # print(self.check_valid(i1, 1))

        if len(s) < 2:
            return len(s)
        l, r = 0, 0
        max_len = 1
        seen_dict = defaultdict(int)
        seen_dict[s[0]] = 1
        while r < len(s)-1:
            r+=1
            seen_dict[s[r]] +=1
            while (self.check_valid(seen_dict, k)) == False:
                seen_dict[s[l]] -=1
                l +=1
                # print(seen_dict)
                # print(l, r)
                
            if r-l+1 > max_len:
                max_len = r-l +1
                # print(l, r)
        return max_len 

        