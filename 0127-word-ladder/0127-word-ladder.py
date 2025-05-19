class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        seen = set()
        alph = "abcdefghijklmnopqrstuvwxyz"

        queue = [(beginWord, 1)]
        while len(queue) > 0:
            prev, count = queue.pop(0)
            for i in range(len(beginWord)):
                for c in alph:
                    nbr = prev[:i] + c + prev[i+1:]
                    if nbr not in seen and nbr in wordSet:
                        if nbr == endWord: return count +1
                        queue.append((nbr, count +1))
                        seen.add(nbr)
        return 0




        