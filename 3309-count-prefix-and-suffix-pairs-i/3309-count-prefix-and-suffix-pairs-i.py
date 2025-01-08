class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if i ==j:
                    continue
                first = words[i]
                second = words[j]
                if first == second[:len(first)] == second[-len(first):]:
                    count +=1
                    # print(first, second)
        return count
        