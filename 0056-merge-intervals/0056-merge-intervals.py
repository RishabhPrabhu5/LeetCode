class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        intervals.sort()
        for interval in intervals:
            if len(ret) == 0 or ret[-1][1] < interval[0]:
                ret.append(interval)
            elif ret[-1][1] >= interval[1]:
                continue
            elif ret[-1][0] < interval[0]:
                ret[-1][1] = interval[1]
            else:
                ret[-1] = interval
        return ret
        

        