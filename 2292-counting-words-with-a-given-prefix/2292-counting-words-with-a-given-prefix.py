class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            if len(pref) <= len(word) and pref == word[:len(pref)]:
                count +=1
        return count
        