class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ones = [i for i in range(len(boxes)) if boxes[i] == "1"]
        ret = [0]*len(boxes)
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(ones)):
                if ones[j] < 0:
                    curr -= ones[j]
                else:
                    curr += ones[j]
                ones[j]-=1
            ret[i] = curr
        return ret
        