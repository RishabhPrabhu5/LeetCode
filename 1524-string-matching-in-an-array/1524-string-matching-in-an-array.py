class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        substrings = []
        for word in words:
            for second in words:
                if second != word and word in second:
                    substrings.append(word)
                    break
        return substrings
        