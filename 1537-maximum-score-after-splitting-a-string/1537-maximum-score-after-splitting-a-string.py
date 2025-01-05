class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = s[1:].count("1")
        max_score = score
        for i in range(0, len(s)-1):
            n = s[i]
            if n == "0":
                score +=1
            elif i >0:
                score -=1
            if score > max_score:
                max_score = score
        return max_score
            
        