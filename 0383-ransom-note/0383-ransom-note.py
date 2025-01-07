class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_map = defaultdict(int)
        rans_map = defaultdict(int)
        for l in magazine:
            mag_map[l] +=1
        for l in ransomNote:
            rans_map[l] += 1
        
        for key in ransomNote:
            if rans_map[key] > mag_map[key]:
                return False
        return True
        


        