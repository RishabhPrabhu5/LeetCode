class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged = []
        curr = intervals[0]
        if len(intervals) ==1:
            return intervals

        for i in range(1, len(intervals)):
            # print(i)
            # print(curr)
            # print(intervals[i])
            # print()
            
            if curr[1]>=intervals[i][0]:
                if curr[1]<=intervals[i][1]:
                    curr = [curr[0], intervals[i][1]]
            else:
                merged.append(curr)
                # print(merged)
                curr = intervals[i]
            if i == len(intervals) -1:
                merged.append(curr)

        return merged

        