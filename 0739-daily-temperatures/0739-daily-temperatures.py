class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []  # will store indices only
        
        for i, temp in enumerate(temperatures):
            # while current temperature is warmer than the temperature
            # at the index on top of the stack
            while stack and temp > temperatures[stack[-1]]:
                day = stack.pop()
                answer[day] = i - day
            
            stack.append(i)
        
        return answer


        