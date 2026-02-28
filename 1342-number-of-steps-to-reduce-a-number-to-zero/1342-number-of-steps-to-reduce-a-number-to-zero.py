class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while True:
            if num == 0:
                return steps
            steps +=1
            if num %2 == 0:
                num /=2
            else:
                num -=1
        return -1

        