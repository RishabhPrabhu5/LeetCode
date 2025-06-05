class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        ret = []
        for word in strs:
            s = "".join(sorted(word))
            if s in dct.keys():
                ret[dct[s]].append(word)
            else:
                ret.append([word])
                dct[s] = len(ret) -1
        return ret

        