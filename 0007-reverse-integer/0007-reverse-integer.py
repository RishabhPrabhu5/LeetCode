class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = x<0
        if is_neg:
            toRet = -1*int(str(x)[::-1][:-1])
            if toRet < -1*(2**31): return 0
            return toRet
        else:
            toRet = int(str(x)[::-1])
            if toRet < 2**31:
                return toRet 
            else:
                return 0
