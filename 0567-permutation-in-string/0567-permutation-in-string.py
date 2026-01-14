class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        target = Counter(s1)
        curr = Counter(s2[:n1])
        
        # Slide window from start to the point where the right edge hits the end
        for i in range(n2 - n1):
            if target == curr:
                return True
            
            # Add next character on the right
            right_char = s2[i + n1]
            curr[right_char] += 1
            
            # Remove character on the left
            left_char = s2[i]
            curr[left_char] -= 1
            if curr[left_char] == 0:
                del curr[left_char]  # Remove key to keep dicts comparable
                
        return target == curr # Final check for the last window

        