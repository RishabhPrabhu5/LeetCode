class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_string = "".join(c for c in s if c.isalnum())
        s =  cleaned_string.lower()
        l = 0
        r = len(s) -1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        