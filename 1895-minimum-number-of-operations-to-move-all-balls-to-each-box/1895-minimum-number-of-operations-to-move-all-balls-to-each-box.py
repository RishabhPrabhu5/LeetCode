class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ret = [0]*len(boxes)

        start = 0
        ones = set()
        diff = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                start += i
                ones.add(i)
                diff +=1
        for i in range(len(boxes)):
            if i in ones:
                diff -=2
            ret[i] = start
            start -= diff
            
        return ret
        