class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        ins = "({["
        outs = ")}]"
        for l in s:
            if l in "({[":
                stack.append(l)
            else:
                if len(stack) == 0:
                    return False
                top_idx = ins.index(stack[-1])
                curr_idx = outs.index(l)
                if curr_idx != top_idx:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
        