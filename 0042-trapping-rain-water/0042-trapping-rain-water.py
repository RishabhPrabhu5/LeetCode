class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = []
        curr = 0
        for num in height:
            curr = max(curr, num)
            max_left.append(curr)
        max_right = []
        curr = 0
        for i in range(len(height)-1, -1, -1):
            curr = max(curr, height[i])
            max_right.insert(0, curr)

        ret = 0
        for i in range(len(height)):
            ret += max(min(max_left[i], max_right[i])-height[i], 0)
        return ret
        