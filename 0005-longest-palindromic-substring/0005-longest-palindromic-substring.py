class Solution(object):

    def checkPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        print(self.checkPalindrome(s))
        max_len = 0
        answer = ""
        curr_len = 0
        curr_ans = ""

        for i in range(len(s)):
            left = i
            right = len(s) -1
            while left<=right:
                if right - left +1 < max_len:
                    break
                if s[left] == s[right] and self.checkPalindrome(s[left+1:right]):
                    curr_len = right-left+1
                    curr_ans = s[left:right+1]
                    if curr_len>max_len:
                        max_len = curr_len
                        answer = curr_ans

                right -=1 

        return answer