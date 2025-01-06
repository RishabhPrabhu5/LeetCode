class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        ans = ""
        for row in range(numRows):
            i = row
            while i < len(s):
                ans += s[i]
                if row>0 and row <numRows -1:
                    other = i+ 2*(numRows-row-1)
                    if  other < len(s):
                        ans += s[other]
                i += 2*(numRows -1)
        return ans
        
        