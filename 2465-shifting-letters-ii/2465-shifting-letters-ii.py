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
        total_shifts = defaultdict(int)
        curr = 0
        for i in range(len(s)):
            curr +=markers[i]
            total_shifts[i] = curr

        to_ret = ""
        for i in total_shifts:
            to_ret += chr((ord(s[i])+total_shifts[i]-97)%26 + 97)
        return to_ret

        