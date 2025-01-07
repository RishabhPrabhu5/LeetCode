class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        substrings = []
        for i in range(len(words)):
            for j in range(len(words)):
                word = words[i]
                second = words[j]
                if second != word and word in second:
                    substrings.append(word)
                    break
        return substrings
        