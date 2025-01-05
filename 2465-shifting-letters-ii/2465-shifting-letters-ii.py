class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        markers = [0]*len(s)
        for shift in shifts:
            if shift[2] == 0:
                markers[shift[0]]+= -1
                if shift[1] < len(s)-1:
                    markers[shift[1]+1] +=1
            else:
                markers[shift[0]]+= 1
                if shift[1] < len(s)-1:
                    markers[shift[1]+1] += -1

        curr = 0
        
        to_ret = list(s)
        for i in range(len(s)):
            curr += markers[i]
            to_ret[i] = chr((ord(s[i])+curr-97)%26 + 97)
        return "".join(to_ret)

        