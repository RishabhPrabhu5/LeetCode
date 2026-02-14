class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack)> 0 and temperatures[i] > stack[-1][0]:
                temp, day = stack.pop()
                answer[day] = i - day

            stack.append((temperatures[i], i))
        return answer


        