class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        prev_t = None
        n = 0
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            t = dist / float(vel)
            if not prev_t or t > prev_t:
                prev_t = t
                n += 1
        return n
        