class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ""
        stack = [s[0]]
        for l in s[1:]:
            if len(stack) > 0 and l.lower() == stack[-1].lower() and l != stack[-1]:
                stack.pop()
            else:
                stack.append(l)
        return "".join(stack)
        