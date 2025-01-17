class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # prefix = strs[0]
        # for s in strs[1:]:
        #     ret = ""
        #     for i in range(min(len(prefix), len(s))):
        #         if prefix[i] == s[i]:
        #             ret += prefix[i]
        #         else:
        #             break
        #     prefix = ret
        # return prefix
        min_len = min([len(s) for s in strs])
        l = len(strs) -1
        ret = ""
        i = 0
        while i < min_len:
            curr = strs[0][i]
            count = 0
            for s in strs[1:]:
                if s[i] == curr:
                    count +=1
            i+=1
            if count == l:
                ret += curr
            else:
                break


        return ret
                
            
        