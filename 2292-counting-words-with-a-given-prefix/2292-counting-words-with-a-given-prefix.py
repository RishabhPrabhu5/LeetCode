class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return sum([1 for word in words if pref == word[:len(pref)]])
        
        